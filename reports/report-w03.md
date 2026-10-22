# Sprint Raporu — Hafta 03 (15.10–20.10.2026)

**Şirket:** Grup B — Logistics Intelligence Network (LIN) / Sevkiyatlar · **PM:** Sude Çukurtaş · **Görev:** Görev 1 — Sektörde Mini Veri Hattı (1. Hafta)

---

## Planlanan

| Issue | Başlık | Atanan | Son tarih | Kabul kriteri |
|---|---|---|---|---|
| #14 | G1-veri — Sektör verisini üret | Sema Coşkun (BE) | 20.10.2026 23:59 | `data/lojistik-sevkiyat.csv` depoda: en az 100 satır (hedef 300), şema `docs/veri-sozlugu-g1.md` içinde yazılı |
| #15 | G1-analiz — Metrikleri hesapla ve bulguları yaz | Aykut Çakıcı (DQ) | 20.10.2026 23:59 | `docs/analiz-g1.md` depoda: en az 5 metrik (en az ikisi kırılımlı), her birinin yorumu ve bulgular bölümü mevcut |
| #16 | G1-gorsel — 2 grafik üret | Ece Naz Aktürk (FE) | 20.10.2026 23:59 | 2 PNG grafik `visuals/` içinde: biri zaman serisi, diğeri kırılım; başlık ve eksen etiketi var; BE verisinden üretilmiş |
| #17 | G1-test — Veri kalitesi testleri | Aykut Çakıcı (DQ) | 20.10.2026 23:59 | `tests/test-cases.md` en az 5 senaryo içeriyor |
| - | Kök `AGENTS.md` + `skills/pm-rapor` + rapor | Sude Çukurtaş (PM) | 20.10.2026 23:59 | Pano günlük kontrolü, `report-w03.md` commit'i, kök dizine `AGENTS.md` |

---

## Yapılan

| Issue | Kanıt (commit / dosya) | Durum |
|---|---|---|
| #14 | `data/lojistik-sevkiyat.csv` (300 satır, 10 alan, tohum 42), `docs/veri-sozlugu-g1.md`, `src/uret_sevkiyat.py`, `skills/be-veri/SKILL.md` — commit `72116d6`, şema güncellemesi `a0e58a2` | ✅ Kapandı |
| #15 | `docs/analiz-g1.md` (5 metrik, kırılımlar ve operasyonel bulgular), `skills/dq-analiz/SKILL.md` — commit `64dd7e3`, `8148f12`, `28975c0` | ✅ Kapandı |
| #16 | `visuals/zaman-serisi.png`, `visuals/kirilim.png`, `src/grafik_uret.py`, `skills/fe-gorsel/SKILL.md` — commit `c41926d` | ✅ Kapandı |
| #17 | `tests/test-cases.md` (8 senaryo), `skills/dq-test/SKILL.md` — commit `7fdbd17`, `cf32e00`, PR #18 (`4f6da24`) | ✅ Kapandı |
| PM | Kök `AGENTS.md` skill envanteri, `skills/pm-rapor/SKILL.md`, `reports/report-w03.md` | ✅ Tamamlandı |

**Öne çıkan sonuçlar (`docs/analiz-g1.md`):** Toplam 300 sevkiyatın 246'sı zamanında teslim (%82 başarı oranı), 39'u gecikmeli (%13), 15'i iptal (%5). Taşıma modları dağılımı: Kara %56, Demiryolu %21, Deniz %14, Hava %9. Ortalama teslim süresi 34.6 saat.

---

## Devir Teslim Zinciri

- **BE → DQ/FE (Veri Teslimi):** Sema veri üretimini tamamlayıp şemayı (`docs/veri-sozlugu-g1.md`) ve `data/lojistik-sevkiyat.csv` dosyasını paylaştı; devir teslim yorumları #15 ve #16'ya yazıldı.
- **DQ → FE (Analiz Teslimi):** Aykut metrik analizini (`docs/analiz-g1.md`, commit `64dd7e3`) tamamlayarak grafik tasarımına yön verecek kırılımları FE Issue'su #16'ya bildirdi.
- **FE → DQ (Görsel ve Test Kontrolü):** Ece 2 PNG grafiği üretip #16 altında sundu; Aykut test senaryolarını (`tests/test-cases.md`) bu çıktılarla eşleştirdi (PR #18).

---

## Tıkanan / Yaşanan Riskler

Hafta boyunca yaşanan ve yönetilen somut tıkanmalar:
1. **Betiğin ve Veri Dosyasının İsimlendirme Uyuşmazlığı:** Veri üretim betiği başlangıçta skill dokümanlarında `src/veri_uret.py` olarak anılırken depodaki dosya `src/uret_sevkiyat.py` idi. Bu durum `AGENTS.md` ve skill dokümanlarında güncellenerek senkronize edildi.
2. **Şema Revizyonu (Ağırlık Aralığı):** DQ incelemesi sırasında lojistik sektör standardına göre `agirlik_kg` aralığının 10–5000 kg olarak genişletilmesi gerektiği tespit edildi. Şema güncellendi ve tohum 42 ile veri yeniden üretilerek commit `a0e58a2` ile depoya yüklendi.
3. **Grafik Zaman Aralığı Kapsamı:** FE'nin planladığı haftalık zaman serisi trendi ilk başta 6 aylık (Ocak-Haziran) bir periyot öngörüyordu; ancak sentetik veri seti 2026 ilk çeyrek (Ocak-Mart) ile sınırlandırıldığı için grafik periyodu ve etiketleri bu 3 aylık veriye uyumlu hale getirildi.

---

## Kim Ne Yaptı

| Üye | Rol | Başlıca Commit'ler / Katkı | Kapattığı Issue |
|---|---|---|---|
| Sude Çukurtaş | PM | Sprint planlama, `AGENTS.md` skill envanteri, `skills/pm-rapor/SKILL.md`, `reports/report-w03.md` | #14-#17 koordinasyonu, #20 |
| Sema Coşkun | BE | `data/lojistik-sevkiyat.csv`, `docs/veri-sozlugu-g1.md`, `src/uret_sevkiyat.py`, `skills/be-veri` (`72116d6`, `a0e58a2`) | #14 |
| Aykut Çakıcı | DQ | `docs/analiz-g1.md`, `skills/dq-analiz`, `tests/test-cases.md`, `skills/dq-test` (`64dd7e3`, `7fdbd17`, PR #18) | #15, #17 |
| Ece Naz Aktürk | FE | `visuals/zaman-serisi.png`, `visuals/kirilim.png`, `src/grafik_uret.py`, `skills/fe-gorsel` (`c41926d`) | #16 |

---

## Gelecek Hafta Planı (Hafta 4 — Görev 1 Kapanışı ve Yan Görev 3)

1. **Test ve Kalite (DQ & Jr):** `tests/test-cases.md` senaryoları `data/lojistik-sevkiyat.csv` üzerinde fiilen çalıştırılacak, sonuçlar `tests/test-log.md` dosyasına tarihli olarak işlenecek; en az 2 hata Issue'su (`bug`) açılacak.
2. **Hata Düzeltmeleri (BE & FE):** Açılan hatalar ilgili geliştiriciler tarafından incelenip commit mesajında `Fixes #no` yazılarak kapatılacak.
3. **Analiz Doğrulama (DQ):** Nihai veri seti `docs/veri-sozlugu-g1.md` ile doğrulanıp onay verilecek.
4. **Sürüm Mühürleme (PM):** Tüm G1 kartlarının kanıtla kapandığı doğrulanacak, `reports/report-w04.md` sprint raporu commit'lenecek ve `gorev1-final` release'i yayınlanacak.
5. **Yan Görev 3 (Çapraz İnceleme):** Partner şirket olan Grup A'nın (`MAKU-VBA-GBT-II/group-a`) reposunda her rol kendi skill incelemesini yapıp Issue açacak.
