# DQ Test Skill'i — G1-TEST

## Amaç

`data/lojistik-sevkiyat.csv` için açık, tekrarlanabilir ve elle uygulanabilir veri kalitesi test senaryoları tanımla. Bu görev senaryoları yazma görevidir; testleri çalıştırma ve sonuçları doldurma Hafta 4'e aittir.

## Gerekli kaynaklar

1. GitHub Issue #17 `G1-TEST` kabul kriterleri.
2. GitHub Issue #14 `G1-SEKTÖR VERİSİ`.
3. BE'nin teslim ettiği `docs/veri-sozlugu-g1.md` ve veri dosyası. Bunlar henüz yoksa önerilen şemaya göre taslak oluştur ve şema kesinleşince güncelle.

## İş akışı

1. Önce Issue #17 ve Issue #14'ü oku.
2. Veri sözlüğündeki alan adlarını, türleri, aralıkları ve kategorileri Issue'lardaki beklentilerle karşılaştır. Çelişki varsa veri sözlüğünü esas al ve belirsizliği senaryoda belirt.
3. `tests/test-cases.md` dosyasına en az beş senaryo yaz. Her senaryo için numara, senaryo adı, adımlar ve beklenen sonucu açıkça belirt.
4. Issue #17'deki dosya, satır sayısı, sütun şeması, tür/aralık ve kategori kontrollerini kapsa. Aynı çıkış-varış şehri olmaması bonus senaryosudur.
5. "Gerçekleşen sonuç" hücresini her senaryoda boş bırak. Test çalıştırma veya başarı iddiası ekleme.
6. Senaryoları veri dosyasını henüz mevcut ve doğru kabul etmeden yaz; beklenen sonucu ölçülebilir şekilde tarif et.

## Çıktı biçimi

`tests/test-cases.md` içinde aşağıdaki sütunları sırayla kullan:

`No | Senaryo | Adımlar | Beklenen sonuç | Gerçekleşen sonuç`

En az beş ana senaryo zorunludur. Ek senaryoları bonus olarak açıkça işaretle. Gerçekleşen sonuç hücreleri boş Markdown hücreleri (`|  |`) olmalıdır.

## Issue #17 kapsamı

- `data/lojistik-sevkiyat.csv` dosyasının bulunması ve okunabilmesi.
- En az 100 veri satırı; hedef 300 satır.
- Şemayla aynı 10 sütun ve sütun sırası/adları.
- `sevkiyat_id` benzersiz olmalı ve `SVK-0001`–`SVK-0300` biçiminde olmalı.
- `tarih` `yyyy-mm-dd` biçiminde, 2026-01-01 ile 2026-03-31 arasında olmalı; `agirlik_kg` 10–5000, `mesafe_km` 50–2500, `ucret_tl` sıfırdan büyük olmalı.
- Şehirler veri sözlüğündeki izinli listede olmalı; çıkış ve varış şehirleri farklı olmalı.
- `tasima_modu`: `kara`, `deniz`, `hava`, `demiryolu`; `durum`: `zamaninda`, `gecikmeli`, `iptal`.
- `durum` değeri `iptal` olan satırlarda `teslim_suresi_saat` boş olmalı; teslim süresi ortalaması hesaplanırken bu satırlar dışarıda tutulmalı.
- Bonus: `cikis_sehri` ve `varis_sehri` aynı olan satır bulunmaması.

## Sınırlar

- Hafta 4'te çalıştırılacak testleri bu görev sırasında çalıştırma veya sonuçlarını tahmin etme.
- Sentetik veri dışında gerçek kişisel veri kullanma.
- BE'nin teslim etmediği dosyaları varmış gibi gösterme.
- Çalışma tamamlandığında Issue #17'ye commit hash'i ve çıktı yollarını bildiren bir devir yorumu hazırla.
