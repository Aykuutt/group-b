name	be-veri

description	Grup B'nin (Lojistik / Sevkiyatlar) sabit tohumlu, tekrarlanabilir sentetik sevkiyat verisini src/uret\_sevkiyat.py ile üretir, şemasını yazar ve DQ/FE'ye devir yorumu bırakır. Veri üretimi yapılacağı zaman kullan.

be-veri — Sentetik sevkiyat verisi üretimi

Ne yapar: G1-veri görevinde Lojistik sektörü için sentetik sevkiyat verisi üretir. Aynı tohum her zaman aynı dosyayı verir. Gerçek kişi veya firma verisi kullanmaz, her şey simülasyondur. Şemasız veri teslim edilmiş sayılmaz.



Girdiler

Depo: MAKU-VBA-GBT-II/group-b

Issue: G1-veri (kabul kriteri ve son tarih orada yazılı)

Tohum: 42, hedef satır sayısı: 300

Şema: DQ ile kesinleştirilmiş alanlar, tipler, aralıklar, kategoriler

Adımlar

Şemayı DQ ile Issue yorumlarında kesinleştir (alan adları, tipler, aralıklar, kategori değerleri, iptal durumunda boş değer kuralı).

src/uret\_sevkiyat.py yaz: sabit tohumlu rastgele sayı üretici kullan, veri data/lojistik-sevkiyat.csv dosyasına yazılsın.

Betiği çalıştır: python src/uret\_sevkiyat.py

Kabul kriterini dosyada kontrol et:

En az 100 satır (hedef 300) var mı?

En az 6 alan (hedef 10) var mı?

tasima\_modu alanında en az 4 farklı değer var mı?

Betik ikinci çalıştırmada birebir aynı dosyayı üretiyor mu?

docs/veri-sozlugu-g1.md dosyasını yaz: her alanın adı, tipi, kuralı, örneği; hedef boyut; tohum; çalıştırma komutu.

Commit mesajı: G1 sevkiyat verisi, şema ve skill eklendi (300 satır). Sonra push.

G1-analiz ve G1-gorsel Issue'larına devir yorumu bırak (aşağıdaki şablon).

G1-veri Issue'suna kanıt yorumu yaz, Issue'yu kapat, kartı Done'a çek.

Devir yorumu şablonu

Veri hazır — commit HASH. Dosya: data/lojistik-sevkiyat.csv, 300 satır, 10 alan. Şema: docs/veri-sozlugu-g1.md. Tohum: 42. Çalıştırma: python src/uret\_sevkiyat.py.



Kullanılan dosyalar

Okur: Issue yorumları (DQ ile şema kararı)

Yazar: src/uret\_sevkiyat.py, data/lojistik-sevkiyat.csv, docs/veri-sozlugu-g1.md

Nasıl çalıştırılır

Ajana (Claude Code, Codex vb.): "be-veri skill'ini kullanarak src/uret\_sevkiyat.py yaz ve veriyi üret." Elle çalıştırmak için: python src/uret\_sevkiyat.py

