---
name: dq-analiz
description: G1 lojistik sevkiyat verisini veri sözlüğüne göre analiz eder, ölçülebilir metrikler ve FE'ye grafik devir önerileri hazırlar.
---

# DQ Analiz Skill'i — G1-ANALİZ

## Amaç

`data/lojistik-sevkiyat.csv` verisini `docs/veri-sozlugu-g1.md` v1.1'e göre analiz et ve sonuçları `docs/analiz-g1.md` içinde raporla. Analiz, sentetik veri hakkında betimleyici sonuçlar üretir; gerçek lojistik operasyonları hakkında nedensellik veya genelleme iddia etmez.

## Kaynaklar

1. GitHub Issue #15 `G1-ANALİZ` kabul kriterleri ve yorumları.
2. GitHub Issue #14 `G1-SEKTÖR VERİSİ` teslim yorumu.
3. `docs/veri-sozlugu-g1.md` ve `data/lojistik-sevkiyat.csv`.
4. Grafik teslimi için GitHub Issue #16 `G1-GÖRSEL`.

## İş akışı

1. Veri teslim yorumundaki commit'i, CSV'yi ve veri sözlüğünün sürümünü doğrula.
2. CSV'yi UTF-8 olarak oku; sütunları veri sözlüğüyle eşleştir ve satır sayısını raporda belirt.
3. Depo kökünden `python src/analiz_g1.py` çalıştır; betiğin hesapladığı değerleri rapora aktar ve kaynağın commit'ini kaydet.
4. Metrikleri aşağıdaki tanımlarla hesapla. Para ve saat değerlerini iki ondalık, yüzdeleri bir ondalık basamakla raporla.
5. Her ana metriğin yanına bir veya iki cümlelik, veriye dayalı yorum yaz.
6. En az üç somut gözlem ve bu gözlemlerden türetilmiş bir eylem önerisi ekle.
7. G1-GÖRSEL Issue #16'ya, analiz commit hash'ini ve grafik için önerilen metrikleri içeren devir yorumu bırak.

## Metrik tanımları

- Toplam ücret: CSV'deki tüm satırların `ucret_tl` değerlerinin toplamı. Rapor, bunun iptal kayıtlarındaki ücretleri de içerdiğini açıkça belirtmelidir.
- Ortalama teslim süresi: `durum=iptal` satırlarını dışarıda bırak; yalnızca sayısal `teslim_suresi_saat` değerlerinin ortalamasını al.
- Taşıma modu kırılımı: Her mod için sevkiyat adedi ve `ucret_tl` ortalamasını göster.
- Varış şehri gecikme kırılımı: Her şehir için toplam kayıt, geciken kayıt ve iptal edilen kayıt sayısını göster. Gecikme oranını `gecikmeli / (zamaninda + gecikmeli) × 100` formülüyle hesapla; paydada iptal kayıtlarını kullanma ve yüzdeyi bir ondalık basamakla raporla. Payda sıfırsa oranı `hesaplanamaz` (veya `—`) olarak göster; `0%` yazma.
- Top-3 varış şehri: `varis_sehri` başına sevkiyat adedini azalan sırada göster; eşitlikte şehir adını alfabetik sırala.
- Aylık sevkiyat adedi: `tarih` alanını `yyyy-mm` düzeyinde grupla. Verinin kapsadığı ayları kullan; bulunmayan aylar için veri varmış gibi değer üretme.

## Çalıştırma

Depo kökünden `python src/analiz_g1.py` komutunu çalıştır. Betik `data/lojistik-sevkiyat.csv` dosyasını okur; toplam ücret, iptal hariç ortalama teslim süresi, mod ve varış şehri kırılımları, top-3 şehir, aylık adetler ve durum dağılımını yazdırır. Betik rapor dosyasını otomatik değiştirmez; sonuçları `docs/analiz-g1.md` ile karşılaştırıp gerektiğinde raporu güncelle.

## Çıktı koşulları

`docs/analiz-g1.md` en az beş metrik içermeli ve toplam, ortalama, iki kırılım ve top-3 beklentilerini karşılamalıdır. Her metrik yorumlanmalı; ayrıca en az üç somut gözlem, bir eylem önerisi, yöntem notları ve FE devir notu yer almalıdır.

G1-GÖRSEL Issue #16 Ocak–Haziran 2026 serisi istiyor; v1.1 veri sözlüğü ve teslim edilen CSV yalnızca 1 Ocak–31 Mart 2026'yı kapsıyor. Yeni veri sağlanana kadar grafikte yalnızca Ocak–Mart göster; bu kapsam farkını FE'ye açıkça bildir.

## Sınırlar

- İptal kayıtlarını teslim süresi ortalamasına katma.
- Eksik aylar veya gözlenmeyen veri için sonuç uydurma.
- Sentetik veriden gerçek dünya nedenselliği veya operasyonel kesinlik çıkarma.
- Test senaryolarını bu analiz skill'iyle çalıştırma; DQ test koşumunu `skills/dq-test/SKILL.md` izler.
