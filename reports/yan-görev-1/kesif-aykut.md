**Repo:** [Platane/snk — GitHub katkı grafiğinden yılan animasyonu üreten araç](https://github.com/Platane/snk)

## Çözdüğü problem

GitHub profilindeki katkı takvimi tek başına yalnızca katkı yoğunluğunu gösteren statik karelerden oluşur. `snk`, bu grafiği yılan animasyonuna dönüştürerek profil README'sinde kullanılabilen hareketli bir SVG veya GIF üretir. Projenin README'sinde aracı Platane geliştiricisinin hazırladığı ve GitHub Actions ile her gün otomatik olarak yeni görsel üretilebildiği anlatılıyor.

## Güçlü yanları

- **Kolay otomasyon:** GitHub Action olarak kullanılabiliyor; kullanıcı adını ve çıktı dosyalarını belirten bir workflow ile üretim otomatikleştirilebiliyor.
- **Özelleştirilebilir çıktı:** SVG ve GIF seçenekleri, farklı renk paletleri ve açık/koyu tema için ayrı görseller destekleniyor. Yalnızca SVG isteyenler için daha hızlı bir Action seçeneği de var.
- **Birden fazla kullanım biçimi:** GitHub Action'ın yanında npm paketi bulunuyor; README, GitHub, GitLab ve Forgejo kaynaklarını destekleyen kullanımı örnekliyor.
- **Açık katkı politikası:** README'de projenin pull request kabul etmediği; sorun bildirimlerinin ve uygulama/API değişikliklerinin önce issue üzerinden konuşulmasının istendiği açıkça belirtiliyor. Bu, her açık kaynak projesinin katkı yönteminin aynı olmadığını gösteriyor.

## Kendi projemde kullanabileceğim fikir

- **Kararım:** `snk` doğrudan sevkiyat hesabı veya lojistik analizi yapmıyor; bu nedenle operasyonel bir özelliği olarak projeye eklemeyi önermiyorum. Ancak ekip reposunun README'sinde, projenin GitHub katkılarını gösteren isteğe bağlı bir görsel olarak kullanılabilir.
- **Uygulama fikri:** GitHub Actions ile görselin otomatik güncellenmesi örnek alınabilir. Bizim repomuzda da rapor veya görselleştirme çıktıları otomatik üretilirse, bu işlem bir workflow ile düzenli ve tekrarlanabilir hale getirilebilir.
- **Öğrendiğim nokta:** Bir repoyu seçmeden önce ne işe yaradığını, nasıl kurulduğunu ve katkı politikasını README'den kontrol etmek gerekiyor. Ayrıca görsel olarak hoş bir araç, her projede doğrudan işlevsel bir ihtiyacı karşılamayabilir.

## Kaynak

- [Platane/snk README](https://github.com/Platane/snk)
- [GitHub Action kullanım örnekleri](https://github.com/Platane/snk#usage)
- [Ders duyurusu: Yan Görev 2](https://github.com/MAKU-VBA-GBT-II/ders/blob/main/Duyuru-4_2026-10-18.md)
