#!/usr/bin/env python3
"""Run the documented G1 shipment data quality scenarios.

Usage from the repository root:
    python src/dq_test.py

Each run prints the observed result for every scenario and refreshes the
automated-run section in tests/test-log.md. The earlier manual run remains in
the log as history.
"""

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from datetime import date, datetime
from decimal import Decimal, InvalidOperation
import hashlib
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "data" / "lojistik-sevkiyat.csv"
LOG_PATH = ROOT / "tests" / "test-log.md"
LOG_START = "<!-- dq_test:results:start -->"
LOG_END = "<!-- dq_test:results:end -->"

EXPECTED_COLUMNS = [
    "sevkiyat_id",
    "tarih",
    "cikis_sehri",
    "varis_sehri",
    "tasima_modu",
    "agirlik_kg",
    "mesafe_km",
    "ucret_tl",
    "teslim_suresi_saat",
    "durum",
]
ALLOWED_CITIES = {
    "Istanbul", "Ankara", "Izmir", "Bursa", "Konya", "Adana", "Antalya"
}
ALLOWED_MODES = {"kara", "deniz", "hava", "demiryolu"}
ALLOWED_STATUSES = {"zamaninda", "gecikmeli", "iptal"}
SHIPMENT_ID = re.compile(r"SVK-(\d{4})\Z")
MIN_DATE = date(2026, 1, 1)
MAX_DATE = date(2026, 3, 31)


@dataclass
class TestResult:
    number: int
    name: str
    actual: str
    passed: bool


def load_csv(path: Path) -> tuple[list[str] | None, list[dict[str, str]] | None, str | None]:
    """Read the shipment CSV without hiding encoding or parse errors."""
    try:
        with path.open("r", encoding="utf-8-sig", newline="") as stream:
            reader = csv.DictReader(stream)
            columns = reader.fieldnames
            rows = list(reader)
        if columns is None:
            return None, None, "CSV başlık satırı bulunamadı"
        if any(None in row for row in rows):
            return columns, rows, "en az bir satır beklenenden fazla sütun içeriyor"
        return columns, rows, None
    except (OSError, UnicodeError, csv.Error) as error:
        return None, None, f"CSV okunamadı: {error}"


def require_rows(rows: list[dict[str, str]] | None, error: str | None) -> tuple[list[dict[str, str]], str | None]:
    if rows is None:
        return [], error or "CSV verisi okunamadı"
    return rows, error


def number_value(row: dict[str, str], field: str) -> Decimal | None:
    raw = (row.get(field) or "").strip()
    if not raw:
        return None
    try:
        value = Decimal(raw)
    except InvalidOperation:
        return None
    return value if value.is_finite() else None


def scenario_results(path: Path) -> tuple[list[TestResult], str]:
    columns, rows, read_error = load_csv(path)
    rows, downstream_error = require_rows(rows, read_error)
    problem = downstream_error or read_error

    results: list[TestResult] = []

    readable = not problem and columns is not None and len(rows) >= 1
    results.append(TestResult(
        1,
        "Sevkiyat dosyası mevcut ve okunabilir",
        f"{len(rows)} veri satırı okundu; başlık: {len(columns or [])} sütun"
        if readable else (problem or "başlık veya veri satırı bulunamadı"),
        readable,
    ))

    results.append(TestResult(
        2,
        "Asgari satır sayısı sağlanıyor",
        f"{len(rows)} veri satırı (alt sınır 100; hedef 300)" if not problem else problem,
        not problem and len(rows) >= 100,
    ))

    header_ok = not problem and columns == EXPECTED_COLUMNS
    results.append(TestResult(
        3,
        "Sütun sayısı ve adları şemayla eşleşiyor",
        f"{len(columns or [])} sütun; beklenen {len(EXPECTED_COLUMNS)} sütun"
        if not problem else problem,
        header_ok,
    ))

    if problem or columns != EXPECTED_COLUMNS:
        id_errors = [problem or "beklenen sütun şeması olmadan ID denetlenemedi"]
    else:
        ids = [(row.get("sevkiyat_id") or "").strip() for row in rows]
        duplicates = len(ids) - len(set(ids))
        bad_ids = []
        for value in ids:
            match = SHIPMENT_ID.fullmatch(value)
            if not match or not 1 <= int(match.group(1)) <= 300:
                bad_ids.append(value or "boş ID")
        id_errors = []
        if duplicates:
            id_errors.append(f"{duplicates} yinelenen ID")
        if bad_ids:
            id_errors.append(f"{len(bad_ids)} biçim/aralık hatası")
    results.append(TestResult(
        4,
        "Sevkiyat kimlikleri benzersiz ve biçime uygun",
        "; ".join(id_errors) if id_errors else f"{len(rows)} ID benzersiz ve SVK-0001–SVK-0300 aralığında",
        not id_errors,
    ))

    numeric_date_errors = 0
    if problem or columns != EXPECTED_COLUMNS:
        numeric_date_errors = 1
    else:
        for row in rows:
            try:
                raw_date = (row.get("tarih") or "").strip()
                parsed = date.fromisoformat(raw_date)
                if parsed.isoformat() != raw_date or not MIN_DATE <= parsed <= MAX_DATE:
                    numeric_date_errors += 1
            except ValueError:
                numeric_date_errors += 1

            weight = number_value(row, "agirlik_kg")
            distance = number_value(row, "mesafe_km")
            fee = number_value(row, "ucret_tl")
            if (weight is None or weight != weight.to_integral_value()
                    or not Decimal("10") <= weight <= Decimal("5000")):
                numeric_date_errors += 1
            if (distance is None or distance != distance.to_integral_value()
                    or not Decimal("50") <= distance <= Decimal("2500")):
                numeric_date_errors += 1
            if fee is None or fee <= 0:
                numeric_date_errors += 1
    results.append(TestResult(
        5,
        "Tarih, tür ve sayısal aralıklar geçerli",
        f"tarih/aralık ihlali: {numeric_date_errors}" if not problem else problem,
        not problem and numeric_date_errors == 0,
    ))

    category_errors: list[str] = []
    if problem or columns != EXPECTED_COLUMNS:
        category_errors.append(problem or "beklenen sütun şeması olmadan kategoriler denetlenemedi")
    else:
        modes = {(row.get("tasima_modu") or "").strip() for row in rows}
        statuses = {(row.get("durum") or "").strip() for row in rows}
        cities = {
            (row.get(field) or "").strip()
            for row in rows
            for field in ("cikis_sehri", "varis_sehri")
        }
        if modes - ALLOWED_MODES:
            category_errors.append(f"izin dışı mod: {sorted(modes - ALLOWED_MODES)}")
        if ALLOWED_MODES - modes:
            category_errors.append(f"eksik mod: {sorted(ALLOWED_MODES - modes)}")
        if statuses - ALLOWED_STATUSES:
            category_errors.append(f"izin dışı durum: {sorted(statuses - ALLOWED_STATUSES)}")
        if cities - ALLOWED_CITIES:
            category_errors.append(f"izin dışı şehir: {sorted(cities - ALLOWED_CITIES)}")
    results.append(TestResult(
        6,
        "Kategoriler ve şehir değerleri geçerli",
        "; ".join(category_errors) if category_errors else "mod, durum ve şehir değerlerinde ihlal yok; dört mod mevcut",
        not category_errors,
    ))

    cancel_errors = 0
    cancelled = 0
    non_cancelled_numeric = 0
    if problem or columns != EXPECTED_COLUMNS:
        cancel_errors = 1
    else:
        for row in rows:
            duration = (row.get("teslim_suresi_saat") or "").strip()
            if (row.get("durum") or "").strip() == "iptal":
                cancelled += 1
                if duration:
                    cancel_errors += 1
            elif number_value(row, "teslim_suresi_saat") is not None:
                non_cancelled_numeric += 1
            else:
                cancel_errors += 1
    results.append(TestResult(
        7,
        "İptal sevkiyatlarda teslim süresi boş",
        f"{cancelled} iptal kaydı boş; {non_cancelled_numeric} iptal olmayan kayıtta süre sayısal; ihlal {cancel_errors}"
        if not problem else problem,
        not problem and cancel_errors == 0,
    ))

    same_city = 0
    if problem or columns != EXPECTED_COLUMNS:
        route_error = problem or "beklenen sütun şeması olmadan rotalar denetlenemedi"
    else:
        same_city = sum(
            (row.get("cikis_sehri") or "").strip() == (row.get("varis_sehri") or "").strip()
            for row in rows
        )
        route_error = f"aynı şehirli rota: {same_city}"
    results.append(TestResult(
        8,
        "Bonus: çıkış ve varış şehirleri farklı",
        route_error,
        not problem and same_city == 0,
    ))

    data_hash = "dosya yok"
    try:
        data_hash = hashlib.sha256(path.read_bytes()).hexdigest()
    except OSError:
        pass
    return results, data_hash


def render_log(results: list[TestResult], data_hash: str) -> str:
    passed = sum(result.passed for result in results)
    date_text = datetime.now().astimezone().date().isoformat()
    rows = [
        LOG_START,
        "## Betikle Otomatik Koşum",
        "",
        f"- Test tarihi: {date_text}",
        "- Komut: `python src/dq_test.py`",
        f"- Test edilen veri SHA-256: `{data_hash}`",
        "",
        "| No | Senaryo | Gerçekleşen sonuç | Durum |",
        "|---:|---|---|---|",
    ]
    for result in results:
        actual = result.actual.replace("|", "\\|")
        status = "Geçti" if result.passed else "Kaldı"
        rows.append(f"| {result.number} | {result.name} | {actual} | {status} |")
    rows.extend(["", f"**Özet:** {passed}/{len(results)} geçti, {len(results) - passed} kaldı.", LOG_END])
    return "\n".join(rows)


def update_log(results: list[TestResult], data_hash: str) -> None:
    if not LOG_PATH.exists():
        raise OSError(f"Test günlüğü bulunamadı: {LOG_PATH.relative_to(ROOT)}")
    content = LOG_PATH.read_text(encoding="utf-8")
    block = render_log(results, data_hash)
    start = content.find(LOG_START)
    end = content.find(LOG_END)
    if start >= 0 and end >= start:
        end += len(LOG_END)
        content = content[:start] + block + content[end:]
    else:
        content = content.rstrip() + "\n\n" + block + "\n"
    with LOG_PATH.open("w", encoding="utf-8", newline="\n") as stream:
        stream.write(content)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--csv",
        type=Path,
        default=CSV_PATH,
        help="CSV yolu (varsayılan: data/lojistik-sevkiyat.csv)",
    )
    args = parser.parse_args()
    path = args.csv if args.csv.is_absolute() else ROOT / args.csv

    try:
        results, data_hash = scenario_results(path)
        try:
            display_path = path.relative_to(ROOT)
        except ValueError:
            display_path = path
        print(f"Test edilen dosya: {display_path}")
        print("Komut: python src/dq_test.py")
        for result in results:
            status = "GEÇTİ" if result.passed else "KALDI"
            print(f"{result.number}. {result.name}: {status} — {result.actual}")
        passed = sum(result.passed for result in results)
        print(f"Özet: {passed}/{len(results)} geçti, {len(results) - passed} kaldı.")
        update_log(results, data_hash)
        print(f"Sonuç günlüğü güncellendi: {LOG_PATH.relative_to(ROOT)}")
        return 0 if passed == len(results) else 1
    except OSError as error:
        print(f"Hata: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())

