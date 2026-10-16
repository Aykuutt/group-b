# G1 Sevkiyat Veri Kalitesi Test Senaryoları

> Taslak, G1-TEST Issue #17 ve G1-SEKTÖR VERİSİ Issue #14'teki önerilen şemaya göre hazırlandı. BE'nin `docs/veri-sozlugu-g1.md` dosyası teslim edildiğinde alan adları, türler ve aralıklar onunla karşılaştırılıp kesinleştirilecektir. Senaryolar Hafta 4'te çalıştırılacaktır.

| No | Senaryo | Adımlar | Beklenen sonuç | Gerçekleşen sonuç |
|---:|---|---|---|---|
| 1 | Sevkiyat dosyası mevcut ve okunabilir | 1. Depoda `data/lojistik-sevkiyat.csv` dosyasının bulunduğunu kontrol et. 2. CSV dosyasını UTF-8 olarak açıp başlık satırını ve en az bir veri satırını okumayı dene. | Dosya belirtilen yolda bulunur; CSV biçiminde açılır ve başlık ile veri satırları okunabilir. |  |
| 2 | Asgari satır sayısı sağlanıyor | 1. CSV'yi başlık satırı hariç veri satırları olarak say. 2. Veri satırı sayısını kaydet. | En az 100 veri satırı vardır; hedeflenen üretim 300 satırdır. |  |
| 3 | Sütun sayısı ve adları şemayla eşleşiyor | 1. CSV başlık satırındaki sütunları sırayla çıkar. 2. Sayıyı ve adları `docs/veri-sozlugu-g1.md` ile karşılaştır. | Tam 10 sütun bulunur ve adlar ile sıraları veri sözlüğündeki şemayla aynıdır: `sevkiyat_id`, `tarih`, `cikis_sehri`, `varis_sehri`, `tasima_modu`, `agirlik_kg`, `mesafe_km`, `ucret_tl`, `teslim_suresi_saat`, `durum`. |  |
| 4 | Zorunlu türler ve sayısal aralıklar geçerli | 1. Her satırda `tarih` değerinin geçerli bir tarihe çevrilebildiğini kontrol et. 2. `agirlik_kg`, `mesafe_km` ve `ucret_tl` değerlerinin sayısal olup olmadığını kontrol et. 3. Ağırlık ve mesafenin sınır değerlerini, ücretin sıfırdan büyük olup olmadığını incele. | Tüm tarihler geçerlidir. `agirlik_kg` 10–5000 kg aralığındadır; `mesafe_km` 50–2500 km aralığındadır; `ucret_tl` 0'dan büyüktür. |  |
| 5 | Kategorik alanlar izin verilen değerleri kullanıyor | 1. `tasima_modu` ve `durum` sütunlarındaki benzersiz değerleri çıkar. 2. Her satırdaki değeri izin verilen kümeyle karşılaştır. | `tasima_modu` yalnızca `kara`, `deniz`, `hava`, `demiryolu` değerlerini; `durum` yalnızca `zamaninda`, `gecikmeli`, `iptal` değerlerini içerir. Dört taşıma modu da veri içinde temsil edilir. |  |
| 6 | Bonus: çıkış ve varış şehirleri farklı | 1. Her satırda `cikis_sehri` ve `varis_sehri` değerlerini karşılaştır. 2. Eşit olan satırların sayısını belirle. | Aynı çıkış ve varış şehrine sahip satır bulunmaz. |  |
