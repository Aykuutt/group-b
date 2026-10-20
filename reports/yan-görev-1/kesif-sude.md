**Repo:** [google/or-tools — Google Optimization Tools](https://github.com/google/or-tools)

## Çözdüğü problem

Lojistikte "hangi araç hangi müşteriye, hangi sırayla gitsin?" sorusunun elle çözülmesi zordur; müşteri sayısı arttıkça olası rota sayısı hızla patlar ve sezgisel planlar hem yolu hem maliyeti gereksiz uzatır. Bu repo, rota planlamayı tahmine bırakmak yerine, açık kaynaklı bir optimizasyon kütüphanesiyle çözer: gezgin satıcı (TSP), araç rotalama (VRP), kapasiteli rotalama (CVRP) ve zaman pencereli rotalama (VRPTW) gibi problemlerde kısıtlara uyan, toplam mesafeyi azaltan rotalar bulur.

## Güçlü yanları

- **Lojistiğe doğrudan uygun:** Araç kapasitesi, müşteri teslimat saat aralığı, çok depo gibi gerçek hayat kısıtları hazır olarak destekleniyor; algoritmayı sıfırdan yazmak gerekmiyor.
- **Ücretsiz ve çok dilli:** Apache 2.0 lisanslı; C++ ile yazılmış ama Python, C# ve Java ile de kullanılabiliyor. Python'da `pip install ortools` ile kurulup birkaç satırla denenebiliyor.
- **Hazır örnek ve dokümantasyon:** `examples` klasöründe rotalama örnekleri, Google'ın geliştirici sitesinde adım adım rehberler var. Ayrıca rotalamanın yanında doğrusal programlama, kısıt programlama ve çizelgeleme çözücüleri de içeriyor.

## Kendi projemde kullanabileceğim fikir

- **Proje lideri olarak karar:** Ekibin ürettiği sipariş verisini (`data/siparisler.csv`) yalnızca üretilip bırakılan bir dosya olmaktan çıkarıp, teslimat maliyetini düşüren bir çıktıya dönüştürmek için "rota optimizasyonu" adımını projeye ek bir görev olarak eklemeyi öneriyorum. OR-Tools hazır olduğu için bu adım için yeni bir algoritma geliştirmeye gerek yok; ekibin işi veriyi doğru hazırlamak ve sonucu ölçmek.
- **Görev dağılımı:** Veri adımından sorumlu kişi, `siparisler.csv` içindeki teslimat noktası ve miktar bilgilerinin OR-Tools'un beklediği biçimde (mesafe matrisi, talepler, araç kapasiteleri) çıktı vermesini sağlar. Rota adımından sorumlu kişi, hazır `lojistik_rota.py` örneğini projenin verisine uyarlar. Rapor adımından sorumlu kişi sonuçları tabloya döker.
- **Başarı ölçütü (liderin belirlediği):** "Elle yapılan rota ile OR-Tools rotası arasındaki toplam mesafe farkı" tek bir net metrik olarak raporlanır. Böylece ekip, çalışmanın işe yarayıp yaramadığını sayıyla gösterebilir.
- **Risk yönetimi:** Mesafelerin tamsayı olması ve mesafe verisinin ayrıca sağlanması gerektiği (OR-Tools haritadan mesafe hesaplamaz) baştan ekibe bildirilir; ilk sürümde basit bir mesafe matrisiyle başlanır, gerçek harita verisi sonraki aşamaya bırakılır.
