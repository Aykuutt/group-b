# Sprint Raporu — Hafta 04 (22.10–27.10.2026)

**Şirket:** Grup B — Logistics Intelligence Network (LIN) / Sevkiyatlar · **PM:** Sude Çukurtaş  
**Tarih:** 22.10.2026  

---

## Planlanan

| Issue | Başlık | Atanan | Son tarih |
|---|---|---|---|
| #24 | [DQ] Hafta 4: Test Koşumu, Hata Tespiti ve Veri Doğrulama | @Aykuutt | 27.10.2026 23:59 |
| #25 | [BE] Hafta 4: Hata Düzeltmeleri ve Nihai Veri Hattı Kapanışı | @sema788 | 27.10.2026 23:59 |
| #26 | [FE] Hafta 4: Görselleştirme Düzeltmeleri ve Çıktı Güncelleme | @ece-naz | 27.10.2026 23:59 |
| #27 | [Junior] Hafta 4: Test Senaryosu Koşma ve Hata Doğrulama | @ipek0-0 | 27.10.2026 23:59 |
| #28 | [Tüm Ekip] Yan Görev 3: Grup A Çapraz Skill İncelemesi | @sudecukurtas, @Aykuutt, @sema788, @ece-naz, @ipek0-0 | 27.10.2026 23:59 |

---

## Yapılan

| Görev / İşlem | Kanıt (commit / dosya / link) | Durum |
|---|---|---|
| Hafta 4 görev kartlarının açılması | Issues #24, #25, #26, #27, #28 | Tamamlandı |
| AGENTS.md büyük harf standardizasyonu | `AGENTS.md` | Tamamlandı |
| Test sonuç günlüğü şablonu | `tests/test-log.md` | Tamamlandı |
| Hafta 4 sprint planlaması | `reports/report-w04.md` | Devam Ediyor |

---

## Devir Teslim Zinciri ve Süreç
- DQ test senaryolarını `data/lojistik-sevkiyat.csv` üzerinde koşarak en az 2 hata Issue'su açacak.
- Veri hataları BE (@sema788), grafik hataları FE (@ece-naz) tarafından düzeltilecek (`Fixes #no` commit mesajıyla).
- Junior üye (@ipek0-0) test koşumuna ve hata yeniden üretimine katılacak.
- Tüm ekip partner şirket olan Grup A'nın (`MAKU-VBA-GBT-II/group-a`) reposunda kendi rolüne ait skill incelemesini tamamlayıp Issue açacak.
- Görev 1 final sürümü için `gorev1-final` release'i yayınlanacak.

---

## Tıkanan / Riskler
- Şu an için açık bir blokaj bulunmamaktadır. Test koşumları ve hata düzeltmeleri sprint takvimine uygun şekilde takip edilmektedir.

---

## Kim Ne Yapacak (Hafta 4 Dağılımı)

| Üye | Rol | Hafta 4 Sorumluluğu |
|---|---|---|
| Sude Çukurtaş | PM | Sprint koordinasyonu, AGENTS.md denetimi, Grup A PM incelemesi, `gorev1-final` release'i |
| Sema Coşkun | BE | Tespit edilen veri hatalarını düzeltme (`Fixes #no`), Grup A BE skill incelemesi |
| Aykut Çakıcı | DQ | `test-cases.md` koşumu, `test-log.md` doldurulması, en az 2 bug Issue'su açılması, veri onaylama, Grup A DQ skill incelemesi |
| Ece Naz Aktürk | FE | Tespit edilen grafik hatalarını düzeltme, nihai PNG çıktılarının güncellenmesi, Grup A FE skill incelemesi |
| İpek Özarslan | Junior | Test koşumu ve hata yeniden üretimi desteği, Grup A incelemesi |
