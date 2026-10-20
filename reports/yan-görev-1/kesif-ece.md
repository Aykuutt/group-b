**Repo:** [visgl/deck.gl — Large-scale WebGL-powered Data Visualization](https://github.com/visgl/deck.gl)

## Çözdüğü problem

Lojistikte yüzlerce aracın, sevkiyat noktasının ve rota hareketinin klasik 2D web haritalarında veya statik tablolarda gösterilmesi tarayıcıları kilitler; DOM elemanları binlerce noktada yavaşlar ve büyük operasyonlar web arayüzünde anlık takip edilemez. Ulaşım devi Uber tarafından açık kaynaklı hale getirilen deck.gl, GPU (WebGL/WebGPU) gücünü doğrudan tarayıcıya getirerek devasa mekânsal (geospatial) lojistik verilerini, sevkiyat koridorlarını ve filo hareketlerini 60 FPS akıcılıkta, 3 boyutlu katmanlar halinde görselleştirmeyi çözer.

## Güçlü yanları

- **Lojistiğe Özel Hazır Katmanlar (Layers):** `ArcLayer` (şehirler ve depolar arası sevkiyat yayları), `TripsLayer` (zamana bağlı animasyonlu araç/sevkiyat rotaları) ve `HeatmapLayer` (teslimat yoğunluk ve gecikme ısı haritaları) gibi lojistik ihtiyaçlara özel katmanları sıfırdan kod yazmadan kullanıma sunar.
- **Yüksek Performans ve Donanım İvmesi:** Hesaplamaları ve render işlemlerini CPU yerine doğrudan kullanıcının ekran kartında (GPU) işlediği için yüz binlerce koordinat ve sevkiyat hareketinde bile tarayıcıda takılma veya gecikme yaşanmaz.
- **Modern Frontend Uyumu:** React, Vue ve modern JavaScript kütüphaneleriyle yerel olarak çalışır; Mapbox veya MapLibre haritalarının üzerine şeffaf bir veri katmanı olarak kolayca entegre edilir.

## Kendi projemde kullanabileceğim fikir

- **Frontend / Görselleştirici rolü olarak karar:** Ekibimizin ürettiği sevkiyat verilerini (`data/lojistik-sevkiyat.csv`) yalnızca statik PNG grafiklerde (`visuals/`) bırakmak yerine, müşteriler ve operasyon yöneticisi için interaktif bir "Sevkiyat Hareket Panosu"na (Dashboard) dönüştürmek için deck.gl'ın `ArcLayer` ve `ScatterplotLayer` katmanlarını kullanmayı öneriyorum.
- **Görev dağılımı ve entegrasyon:** BE (Backend) veri üreticisi sevkiyat verisine çıkış/varış koordinatlarını (enlem/boylam) ekler; FE (Frontend) olarak ben bu veriyi deck.gl katmanlarına bağlayarak teslimat durumlarına göre (zamanında teslim edilenler yeşil, gecikenler kırmızı yaylar) 3D haritada canlandırırım; DQ ekibi ise haritada görselleştirilen gecikme yoğunluklarının analiz doğruluğunu test eder.
- **Başarı ölçütü (FE rolünün belirlediği):** Sevkiyat akışının ve geciken rotaların tek bir interaktif harita üzerinde operasyon ekibi tarafından 1 saniyeden kısa sürede filtrelenip görsel olarak teşhis edilebilmesi.
- **Risk yönetimi:** deck.gl'ın GPU gereksinimi nedeniyle düşük donanımlı tarayıcılarda performans düşüşü yaşanmaması için hafifletilmiş 2D görünümler (fallback) kurgulanmalı ve ilk aşamada karmaşık animasyonlar yerine statik `ArcLayer` yaylarıyla başlanmalıdır.
