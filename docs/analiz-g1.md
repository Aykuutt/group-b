# G1 Sevkiyat Analizi

**Kaynak:** `data/lojistik-sevkiyat.csv` · **Şema:** `docs/veri-sozlugu-g1.md` v1.1 · **Kayıt:** 300 sevkiyat · **Dönem:** 1 Ocak–31 Mart 2026

Bu rapordaki veriler sabit tohum 42 ile üretilmiş sentetik kayıtlardır. Bulgular yalnızca bu veri kümesini betimler; gerçek operasyonlar için nedensellik veya genelleme göstermez.

## Metrikler ve yorumlar

### 1. Toplam kayıtlı taşıma ücreti

| Metrik | Sonuç |
|---|---:|
| 300 satırdaki `ucret_tl` toplamı | 1.488.869,89 TL |

Toplam, CSV'de bulunan 300 satırın ücretlerini toplar ve iptal durumundaki 12 kaydın ücretlerini de içerir. İptal ücretlerinin finansal raporlamada nasıl ele alınacağı veri sözlüğünde ayrıca tanımlanmadığından bu toplam kayıtlı ücret toplamı olarak okunmalıdır.

### 2. Ortalama teslim süresi

| Metrik | Sonuç |
|---|---:|
| İptal olmayan teslimat sayısı | 288 |
| Ortalama teslim süresi | 20,42 saat |

Ortalama, yalnızca `zamaninda` veya `gecikmeli` durumundaki 288 kaydın `teslim_suresi_saat` değerleriyle hesaplandı. İptal edilen 12 kaydın süresi boş olduğu için ortalamaya katılmadı.

### 3. Taşıma moduna göre sevkiyat adedi ve ortalama ücret

| Taşıma modu | Sevkiyat | Toplam içindeki pay | Ortalama ücret |
|---|---:|---:|---:|
| Kara | 157 | %52,3 | 4.476,02 TL |
| Demiryolu | 60 | %20,0 | 2.850,24 TL |
| Deniz | 45 | %15,0 | 1.823,49 TL |
| Hava | 38 | %12,7 | 14.028,00 TL |

Kara taşımacılığı sevkiyatların yarıdan fazlasını oluşturur. Hava modunun kayıt başına ortalama ücreti en yüksektir; ücretler ağırlık ve mesafeye de bağlı olduğundan bu fark tek başına mod verimliliğini göstermez.

### 4. Varış şehrine göre gecikme oranı

Gecikme oranı = geciken sevkiyat / (zamanında + gecikmeli sevkiyat). İptaller paydaya alınmamıştır.

| Varış şehri | Toplam kayıt | Geciken | İptal | İptal olmayanlar içinde gecikme oranı |
|---|---:|---:|---:|---:|
| Adana | 27 | 8 | 0 | %29,6 |
| Bursa | 34 | 9 | 1 | %27,3 |
| Izmir | 71 | 13 | 4 | %19,4 |
| Ankara | 60 | 11 | 3 | %19,3 |
| Antalya | 27 | 5 | 1 | %19,2 |
| Istanbul | 56 | 10 | 2 | %18,5 |
| Konya | 25 | 3 | 1 | %12,5 |

Adana ve Bursa bu veri kümesinde en yüksek gecikme oranlarına sahiptir. Bu oranlar küçük, sentetik şehir örneklerine dayandığı için gerçek rota performansı olarak yorumlanmamalıdır.

### 5. En çok sevkiyat alan ilk üç varış şehri

| Sıra | Varış şehri | Sevkiyat | Toplam içindeki pay |
|---:|---|---:|---:|
| 1 | Izmir | 71 | %23,7 |
| 2 | Ankara | 60 | %20,0 |
| 3 | Istanbul | 56 | %18,7 |

İlk üç varış şehri toplam 187 sevkiyat alır; bu, veri kümesinin %62,3'üdür. Görselleştirmede yoğunluk bu şehirlerde belirgin biçimde toplanır.

### 6. Aylık sevkiyat sayısı

| Ay | Sevkiyat |
|---|---:|
| Ocak 2026 | 99 |
| Şubat 2026 | 98 |
| Mart 2026 | 103 |

Üç ayın hacmi birbirine yakındır ve aylık aralık 98–103 sevkiyattır. Bu seri yalnızca CSV'de bulunan Ocak–Mart dönemini kapsar.

### Durum dağılımı

| Durum | Sevkiyat | 300 kayıt içindeki pay |
|---|---:|---:|
| Zamanında | 229 | %76,3 |
| Gecikmeli | 59 | %19,7 |
| İptal | 12 | %4,0 |

## Somut gözlemler

1. İptal olmayan sevkiyatlar arasında en yüksek gecikme oranı Adana'da %29,6 (8/27), ardından Bursa'da %27,3'tür (9/33); en düşük oran Konya'da %12,5'tir (3/24).
2. Hava taşımacılığında ortalama ücret 14.028,00 TL ile modlar arasındaki en yüksek değerdir; kara taşımacılığında ortalama 4.476,02 TL'dir. Bu karşılaştırma ağırlık ve mesafe dağılımından bağımsız bir maliyet/verimlilik sonucu vermez.
3. Izmir, Ankara ve Istanbul toplam 187 sevkiyatla kayıtların %62,3'ünü alır; görsel özet bu yoğunlaşmayı gösterebilir.

## Eylem önerisi

Gerçek operasyon verisi geldiğinde Adana ve Bursa varışlı geciken kayıtları rota, taşıma modu ve mesafe bazında inceleyip gecikme kaynaklarını doğrulayın. Bu sentetik veriyle operasyonel değişiklik kararı vermeyin.

## FE devir notu — G1-GÖRSEL #16

- Zaman serisi için aylık sevkiyat sayıları: Ocak 99, Şubat 98, Mart 103.
- Kırılım grafiği için taşıma moduna göre ortalama ücret: kara 4.476,02 TL; deniz 1.823,49 TL; hava 14.028,00 TL; demiryolu 2.850,24 TL.
- Kapsam farkı: G1-GÖRSEL Issue #16 Ocak–Haziran 2026'yı istiyor; mevcut veri yalnızca Ocak–Mart dönemini kapsıyor. İlave veri teslim edilmedikçe grafikte Ocak–Mart gösterilmeli ve eksik aylar için değer üretilmemeli.

