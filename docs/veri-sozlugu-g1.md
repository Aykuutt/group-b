\# Veri Sözlüğü — Lojistik Sevkiyat Verisi (Görev 1)

\*\*Sürüm:\*\* v1 · \*\*BE:\*\* Sema Coşkun · \*\*DQ:\*\* Aykut Çakıcı · \*\*Tarih:\*\* 2026-10-17



\## Veri Kümesi: data/lojistik-sevkiyat.csv

| Alan | Tip | Kural/Aralık | Örnek |

|---|---|---|---|

| sevkiyat\_id | Metin | SVK-0001 ... SVK-0300, benzersiz | SVK-0001 |

| tarih | Tarih | yyyy-mm-dd, 2026-01-01 ile 2026-03-31 arası | 2026-02-14 |

| cikis\_sehri | Metin | Istanbul, Ankara, Izmir, Bursa, Konya, Adana, Antalya | Ankara |

| varis\_sehri | Metin | cikis\_sehri ile aynı liste, farklı şehir | Izmir |

| tasima\_modu | Metin | kara / deniz / hava / demiryolu | kara |

| agirlik\_kg | Tam sayı | 50-5000 | 1200 |

| mesafe\_km | Tam sayı | rotaya bağlı; hava modunda karayolunun %85'i | 450 |

| ucret\_tl | Ondalık | agirlik x mesafe x mod katsayısı, 2 basamak | 2160.00 |

| teslim\_suresi\_saat | Ondalık | mesafe/hız + bekleme (gecikmeliyse ek süre), 1 basamak; durum=iptal ise BOŞ | 14.3 |

| durum | Metin | zamaninda / gecikmeli / iptal | zamaninda |



\*\*Hedef boyut:\*\* 300 satır + başlık · \*\*Tohum:\*\* 42 · \*\*Ayraç:\*\* virgül · \*\*Kodlama:\*\* UTF-8

\*\*Üretim:\*\* `python src/uret\_sevkiyat.py`



\## Notlar

\- Veri tamamen simülasyondur, gerçek kişi veya firma verisi yoktur.

\- Taşıma modu, şehirlerin liman/havalimanı durumuna bakılmadan atanır (basitleştirme).



\## Değişiklik Günlüğü

\- v1 — ilk sürüm (2026-10-17)

