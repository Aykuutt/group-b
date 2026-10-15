---
name: pm-rapor
description: Grup B'nin (Lojistik / Sevkiyatlar) haftalık sprint raporunu reports/report-wXX.md dosyasına GitHub izlerinden (Issue, commit, pano) derler. Haftalık rapor yazılacağı zaman kullan.
---

# pm-rapor — Haftalık sprint raporu

**Ne yapar:** Belirtilen haftanın sprint raporunu depodaki gerçek izlere (Issue'lar, kanıt yorumları, commit'ler, proje panosu) dayanarak `reports/report-wXX.md` dosyasına yazar. Uydurma bilgi yazmaz; her iddia bir Issue numarasına veya commit hash'ine bağlanır.

## Girdiler

- Hafta numarası (örn. `03`) ve haftanın tarih aralığı
- Depo: `MAKU-VBA-GBT-II/group-b`
- O haftanın Issue'ları: G1-veri, G1-analiz, G1-gorsel, G1-test
- Proje panosu: <Logistics Intelligence Network (LIN) grup-b panosu> (To Do → In Progress → Done)

## Adımlar

1. **Planlananları topla:** Issue'ları listele (numara, başlık, atanan kişi, son tarih, kabul kriteri).
2. **Yapılanları doğrula:** Her Issue için kanıt yorumunu ve ilgili commit'i bul. Kabul kriterini dosyada gerçekten kontrol et:
   - `data/sevkiyat-verisi.csv` var mı, en az 100 satır mı?
   - `docs/analiz-g1.md` içinde en az 5 metrik ve bulgular bölümü var mı?
   - `visuals/` içinde 2 PNG var mı?
   - `tests/test-cases.md` içinde en az 5 senaryo var mı?
3. **Devir teslim zincirini kontrol et:** BE → DQ/FE ("Veri hazır" yorumu G1-analiz ve G1-gorsel'de var mı?) ve DQ → FE ("Analiz hazır" yorumu G1-gorsel'de var mı?).
4. **Tıkananları yaz:** Açık kalan Issue'lar, kaçırılan son tarihler, bekleyen devir teslimler ve nedenleri.
5. **Kim ne yaptı:** Her üye için commit sayısı ve kapattığı Issue'lar.
6. Raporu aşağıdaki şablonla `reports/report-wXX.md` olarak yaz; commit mesajı: `Hafta XX sprint raporu eklendi`.

## Şablon

```markdown
# Sprint Raporu — Hafta XX (GG.AA–GG.AA.YYYY)

**Şirket:** Grup B — Lojistik / Sevkiyatlar · **PM:** <PM adı>

## Planlanan
| Issue | Başlık | Atanan | Son tarih |
|---|---|---|---|

## Yapılan
| Issue | Kanıt (commit / dosya) | Durum |
|---|---|---|

## Devir teslim zinciri
- BE → DQ/FE: …
- DQ → FE: …

## Tıkanan / riskler
- …

## Kim ne yaptı
| Üye | Rol | Commit | Kapattığı Issue |
|---|---|---|---|

## Gelecek hafta
- …
```

## Kullanılan dosyalar

- Okur: GitHub Issue'ları ve yorumları, `git log`, proje panosu
- Yazar: `reports/report-wXX.md`

## Nasıl çalıştırılır

Ajana (Claude Code, Codex vb.): **"pm-rapor skill'ini kullanarak Hafta 03 için report-w03.md yaz."** Ajan GitHub'a erişemezse Issue listesi ve `git log --since=... --pretty='%h %an %s'` çıktısı ona verilir.
