# G1 Sevkiyat Veri Kalitesi Test Sonuç Günlüğü (test-log.md)

**Şirket:** Grup B — Logistics Intelligence Network (LIN)  
**Test Edilen Dosya:** `data/lojistik-sevkiyat.csv`  
**Referans:** `tests/test-cases.md`, `docs/veri-sozlugu-g1.md` v1.1  
**Test edilen upstream kaynak:** `main` @ `8962c03ba82cb214b28405cfd27295d1cea8246b` (CSV dosyası bu commit'te)  
**Test yöntemi:** İlk koşum 2026-10-22'de elle yapıldı. Tekrarlanabilir sonraki koşumlar için `python src/dq_test.py` kullanılır; betik her senaryonun gerçekleşen sonucunu ve durumunu aşağıdaki otomatik koşum bölümüne yazar.
**Test Eden:** Aykut Çakıcı (DQ)

---

## Test Koşum Kayıtları

| No | Senaryo | Test Tarihi | Test Eden | Gerçekleşen Sonuç | Durum (Geçti / Kaldı) | İlgili Issue / Not |
|---:|---|---|---|---|---|---|
| 1 | Sevkiyat dosyası mevcut ve okunabilir | 2026-10-22 | Aykut Çakıcı (DQ) | UTF-8 CSV okundu; 10 sütun ve 300 veri satırı | Geçti | — |
| 2 | Asgari satır sayısı sağlanıyor | 2026-10-22 | Aykut Çakıcı (DQ) | 300 veri satırı (hedef 300; alt sınır 100) | Geçti | — |
| 3 | Sütun sayısı ve adları şemayla eşleşiyor | 2026-10-22 | Aykut Çakıcı (DQ) | 10 sütun; adlar ve sıra veri sözlüğü v1.1 ile birebir aynı | Geçti | — |
| 4 | Sevkiyat kimlikleri benzersiz ve biçime uygun | 2026-10-22 | Aykut Çakıcı (DQ) | 300 benzersiz ID; SVK-0001–SVK-0300 aralığında | Geçti | — |
| 5 | Tarih, tür ve sayısal aralıklar geçerli | 2026-10-22 | Aykut Çakıcı (DQ) | Tarihler 2026-01-01–2026-03-31; ağırlık 10–5000, mesafe 50–2500, ücret > 0; ihlal 0 | Geçti | — |
| 6 | Kategoriler ve şehir değerleri geçerli | 2026-10-22 | Aykut Çakıcı (DQ) | Şehir/durum/mod değerlerinde şema dışı kayıt 0; dört mod da mevcut | Geçti | — |
| 7 | İptal sevkiyatlarda teslim süresi boş | 2026-10-22 | Aykut Çakıcı (DQ) | 12 iptal satırının teslim süresi boş; iptal olmayan 288 satırda süre sayısal | Geçti | İptaller ortalamadan hariç |
| 8 | Bonus: çıkış ve varış şehirleri farklı | 2026-10-22 | Aykut Çakıcı (DQ) | Aynı şehirli rota 0 | Geçti | — |

**Özet:** 8 senaryo, 8 geçti, 0 kaldı. Hata bulunmadı; Duyuru 5 gereği iki somut enhancement önerisi açılmalı. Öneriler: tekrar kullanılabilir DQ test betiği ve CSV yazılmadan önce üretici şema doğrulaması.

---

## Test Edilen Nihai Veri

- 300 satır, 10 beklenen alan; dosya UTF-8 ve virgülle ayrılmış.
- 300 benzersiz ve biçime uygun sevkiyat kimliği.
- Tarih, ağırlık, mesafe ve ücret kurallarında ihlal yok.
- İzinli şehir, durum ve taşıma modları dışında değer yok; dört modun tamamı mevcut.
- 12 iptal kaydında teslim süresi boş; iptal olmayan 288 kayıtta sayısal.
- Çıkış ve varış şehirleri aynı olan kayıt yok.

---

## İyileştirme Önerileri

1. `tests/test-cases.md` senaryolarını tekrarlanabilir biçimde çalıştıran `src/dq_test.py` eklenmesi.
2. `src/uret_sevkiyat.py` içinde CSV yazılmadan önce tüm veri sözlüğü kurallarının doğrulanması.

## Tespit Edilen Hatalar ve Açılan Kayıtlar

- Veri hatası tespit edilmedi; test sonucu 8/8 geçti.
- İki somut iyileştirme önerisi Duyuru 5 kapsamında açıldı: tekrar kullanılabilir DQ test betiği (#38) ve üretim öncesi şema doğrulaması (#39).

<!-- dq_test:results:start -->
## Betikle Otomatik Koşum

- Test tarihi: 2026-10-24
- Komut: `python src/dq_test.py`
- Test edilen veri SHA-256: `432a739590d20b9a9fee7d6cfd0b521c339107da80b1308593359e7d0ae5a727`

| No | Senaryo | Gerçekleşen sonuç | Durum |
|---:|---|---|---|
| 1 | Sevkiyat dosyası mevcut ve okunabilir | 300 veri satırı okundu; başlık: 10 sütun | Geçti |
| 2 | Asgari satır sayısı sağlanıyor | 300 veri satırı (alt sınır 100; hedef 300) | Geçti |
| 3 | Sütun sayısı ve adları şemayla eşleşiyor | 10 sütun; beklenen 10 sütun | Geçti |
| 4 | Sevkiyat kimlikleri benzersiz ve biçime uygun | 300 ID benzersiz ve SVK-0001–SVK-0300 aralığında | Geçti |
| 5 | Tarih, tür ve sayısal aralıklar geçerli | tarih/aralık ihlali: 0 | Geçti |
| 6 | Kategoriler ve şehir değerleri geçerli | mod, durum ve şehir değerlerinde ihlal yok; dört mod mevcut | Geçti |
| 7 | İptal sevkiyatlarda teslim süresi boş | 12 iptal kaydı boş; 288 iptal olmayan kayıtta süre sayısal; ihlal 0 | Geçti |
| 8 | Bonus: çıkış ve varış şehirleri farklı | aynı şehirli rota: 0 | Geçti |

**Özet:** 8/8 geçti, 0 kaldı.
<!-- dq_test:results:end -->

