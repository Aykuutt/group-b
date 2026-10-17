# Veri Sözlüğü — Lojistik Sevkiyat Verisi (Görev 1)
**Sürüm:** v1.1 · **BE:** Sema Coşkun · **DQ:** Aykut Çakıcı · **Tarih:** 2026-10-17

## Veri Kümesi: data/lojistik-sevkiyat.csv
| Alan | Tip | Kural/Aralık | Örnek |
|---|---|---|---|
| sevkiyat_id | Metin | SVK-0001 ... SVK-0300, benzersiz | SVK-0001 |
| tarih | Tarih | yyyy-mm-dd, 2026-01-01 ile 2026-03-31 arası | 2026-02-14 |
| cikis_sehri | Metin | Istanbul, Ankara, Izmir, Bursa, Konya, Adana, Antalya | Ankara |
| varis_sehri | Metin | cikis_sehri ile aynı liste, farklı şehir | Izmir |
| tasima_modu | Metin | kara / deniz / hava / demiryolu | kara |
| agirlik_kg | Tam sayı | 10-5000 | 1200 |
| mesafe_km | Tam sayı | rotaya bağlı; hava modunda karayolunun %85'i | 450 |
| ucret_tl | Ondalık | agirlik x mesafe x mod katsayısı, 2 basamak | 2160.00 |
| teslim_suresi_saat | Ondalık | mesafe/hız + bekleme (gecikmeliyse ek süre), 1 basamak; durum=iptal ise BOŞ; teslim süresi ortalamasında iptaller hariç tutulur | 14.3 |
| durum | Metin | zamaninda / gecikmeli / iptal | zamaninda |

**Hedef boyut:** 300 satır + başlık · **Tohum:** 42 · **Ayraç:** virgül · **Kodlama:** UTF-8
**Üretim:** `python src/uret_sevkiyat.py`

## Notlar
- Veri tamamen simülasyondur, gerçek kişi veya firma verisi yoktur.
- Taşıma modu, şehirlerin liman/havalimanı durumuna bakılmadan atanır (basitleştirme).

## Değişiklik Günlüğü
- v1 — ilk sürüm (2026-10-17)
- v1.1 — agirlik_kg aralığı 10-5000 kg yapıldı (DQ Aykut Çakıcı kararı, #17 test kriteriyle tutarlılık); teslim süresi ortalamasında iptallerin hariç tutulduğu eklendi (2026-10-17)