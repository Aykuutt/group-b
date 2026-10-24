#!/usr/bin/env python3
"""G1 sevkiyat analiz metriklerini veri sözlüğüne göre hesaplar.

Kullanım (depo kökünden):
    python src/analiz_g1.py

Çıktı yalnızca betimleyici sentetik veri özetidir; operasyonel genelleme değildir.
"""
from collections import Counter, defaultdict
from datetime import date
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "data" / "lojistik-sevkiyat.csv"
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
CENT = Decimal("0.01")


def money(value):
    """Decimal sonucu iki basamağa yuvarla."""
    return value.quantize(CENT, rounding=ROUND_HALF_UP)


def load_shipments(path=CSV_PATH):
    """CSV'yi UTF-8 oku ve beklenen alan sırasını doğrula."""
    with path.open("r", encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream)
        if reader.fieldnames != EXPECTED_COLUMNS:
            raise ValueError(
                "CSV sütunları veri sözlüğüyle eşleşmiyor: "
                f"{reader.fieldnames!r}"
            )
        rows = list(reader)

    if not rows:
        raise ValueError(f"CSV'de veri satırı yok: {path}")
    return rows


def decimal_value(row, field):
    """Gerekli sayısal alanı güvenli şekilde Decimal'e çevir."""
    value = row[field].strip()
    if not value:
        raise ValueError(f"{row['sevkiyat_id']}: {field} boş")
    try:
        return Decimal(value)
    except InvalidOperation as error:
        raise ValueError(
            f"{row['sevkiyat_id']}: {field} sayısal değil: {value!r}"
        ) from error


def calculate(rows):
    """Analiz raporundaki metrikleri deterministik olarak hesapla."""
    total_fee = sum(
        (decimal_value(row, "ucret_tl") for row in rows), Decimal("0")
    )
    delivered = [
        row for row in rows
        if row["durum"] != "iptal" and row["teslim_suresi_saat"].strip()
    ]
    delivery_total = sum(
        (decimal_value(row, "teslim_suresi_saat") for row in delivered),
        Decimal("0"),
    )

    modes = defaultdict(lambda: {"count": 0, "fee_total": Decimal("0")})
    arrivals = defaultdict(lambda: {"total": 0, "late": 0, "cancelled": 0})
    months = Counter()
    statuses = Counter()

    for row in rows:
        mode = modes[row["tasima_modu"]]
        mode["count"] += 1
        mode["fee_total"] += decimal_value(row, "ucret_tl")

        arrival = arrivals[row["varis_sehri"]]
        arrival["total"] += 1
        if row["durum"] == "gecikmeli":
            arrival["late"] += 1
        elif row["durum"] == "iptal":
            arrival["cancelled"] += 1

        try:
            shipment_date = date.fromisoformat(row["tarih"])
        except ValueError as error:
            raise ValueError(
                f"{row['sevkiyat_id']}: geçersiz tarih {row['tarih']!r}"
            ) from error
        months[shipment_date.strftime("%Y-%m")] += 1
        statuses[row["durum"]] += 1

    return {
        "row_count": len(rows),
        "total_fee": total_fee,
        "delivered_count": len(delivered),
        "average_delivery": delivery_total / len(delivered),
        "modes": modes,
        "arrivals": arrivals,
        "top_destinations": sorted(
            arrivals.items(), key=lambda item: (-item[1]["total"], item[0])
        )[:3],
        "months": sorted(months.items()),
        "statuses": statuses,
    }


def print_report(metrics):
    """Metrikleri okunabilir, tekrar üretilebilir biçimde yazdır."""
    print(f"Veri dosyası: {CSV_PATH.relative_to(ROOT)}")
    print(f"Sevkiyat sayısı: {metrics['row_count']}")
    print(f"Toplam kayıtlı ücret: {money(metrics['total_fee']):.2f} TL")
    print(
        "Ortalama teslim süresi (iptaller hariç, "
        f"{metrics['delivered_count']} kayıt): "
        f"{money(metrics['average_delivery']):.2f} saat"
    )

    print("\nTaşıma modu (adet, ortalama ücret):")
    for mode, values in sorted(metrics["modes"].items()):
        average_fee = values["fee_total"] / values["count"]
        print(
            f"- {mode}: {values['count']}, "
            f"{money(average_fee):.2f} TL"
        )

    print("\nVarış şehrine göre gecikme (toplam, geciken, iptal, oran):")
    for city, values in sorted(metrics["arrivals"].items()):
        non_cancelled = values["total"] - values["cancelled"]
        late_rate = (
            Decimal(values["late"]) * Decimal("100") / Decimal(non_cancelled)
            if non_cancelled
            else None
        )
        rate_text = (
            f"{late_rate.quantize(Decimal('0.1')):.1f}%"
            if late_rate is not None
            else "hesaplanamaz"
        )
        print(
            f"- {city}: {values['total']}, {values['late']}, "
            f"{values['cancelled']}, {rate_text}"
        )

    print("\nEn çok sevkiyat alan ilk 3 varış şehri:")
    for rank, (city, values) in enumerate(metrics["top_destinations"], start=1):
        print(f"{rank}. {city}: {values['total']}")

    print("\nAylık sevkiyat sayısı:")
    for month, count in metrics["months"]:
        print(f"- {month}: {count}")

    print("\nDurum dağılımı:")
    for status, count in sorted(metrics["statuses"].items()):
        print(f"- {status}: {count}")


def main():
    rows = load_shipments()
    print_report(calculate(rows))


if __name__ == "__main__":
    main()
