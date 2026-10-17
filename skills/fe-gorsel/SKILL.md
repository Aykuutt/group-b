---
name: fe-gorsel
description: G1 lojistik sevkiyat verisi ve DQ analiz metriklerine göre standartlara uygun zaman serisi ve taşıma modu kırılım grafiklerini üretir.
---

# FE Görsel Skill'i — G1-GÖRSEL

## Amaç

`data/lojistik-sevkiyat.csv` verisini ve `docs/analiz-g1.md` analiz sonuçlarını girdi alarak, proje görsel standartlarına tam uyumlu iki adet yüksek çözünürlüklü grafik (`visuals/zaman-serisi.png` ve `visuals/kirilim.png`) üretmek.

## Kaynaklar ve Bağımlılıklar

1. **GitHub Issue #16 (`G1-GÖRSEL`):** Kabul kriterleri ve görsel gereksinimleri.
2. **G1-Veri Devir Yorumu (`#16`):** `@sema788` (BE) veri devir teslimi (Commit: `a0e58a2`, `data/lojistik-sevkiyat.csv`, şema `docs/veri-sozlugu-g1.md` v1.1).
3. **G1-Analiz Devir Yorumu (`#16`):** `@Aykuutt` (DQ) analiz devir teslimi (Commit: `64dd7e3`, `docs/analiz-g1.md`).
4. **Veri Kümesi:** `data/lojistik-sevkiyat.csv` (300 kayıt).
5. **Analiz ve Metrikler:** `docs/analiz-g1.md`.

## Önkoşullar ve Uyumsuzluk Yönetimi

1. **Devir Sıralaması:**
   - Taslak çizimine başlamak için BE'nin `G1-veri devir yorumu` şarttır.
   - Grafik bölümlerini ve kesin değerlerini netleştirmek için DQ'nun `G1-analiz devir yorumu` şarttır.
   - Her iki devir de Issue #16 üzerinde tamamlanmıştır.
2. **Taslaksız Başlangıç Yasağı:**
   - Nihai grafikler üretilip commit edilmeden önce, grafiklerin yerleşimini ve eksenlerini gösteren bir taslak ekran görüntüsü GitHub Issue #16'ya yüklenmelidir.
3. **Kapsam Uyumsuzluğu Kuralı:**
   - Issue açıklamasındaki planlanan başlıkta *"Ocak–Haziran 2026"* ifadesi geçmektedir; ancak `docs/veri-sozlugu-g1.md` ve `docs/analiz-g1.md` ile doğrulanmış veri kümesi yalnızca **1 Ocak–31 Mart 2026** dönemini içermektedir.
   - Proje kuralları gereği sentetik veri uydurulmaz veya tahmin üretilmez.
   - Bu nedenle zaman serisi grafiği **"Aylık Sevkiyat Sayısı (Ocak–Mart 2026)"** başlığı ve kapsamıyla üretilir.

## Grafik Tanımları ve Standartları

### 1. Zaman Serisi Grafiği (`visuals/zaman-serisi.png`)
* **Grafik Türü:** Çizgi grafik (Line chart) ile vurgulanmış veri noktaları (markers).
* **Başlık:** Aylık Sevkiyat Sayısı (Ocak–Mart 2026)
* **X Ekseni:** Ay (Ocak 2026, Şubat 2026, Mart 2026)
* **Y Ekseni:** Sevkiyat Adedi (adet)
* **Veri Değerleri:**
  * Ocak 2026: 99
  * Şubat 2026: 98
  * Mart 2026: 103
* **Özellikler:** Her noktanın üzerinde tam sayı veri etiketi yer almalı, trend çizgisi kurumsal mavi renkte ve kılavuz çizgileriyle (grid) desteklenmelidir.

### 2. Taşıma Modu Kırılım Grafiği (`visuals/kirilim.png`)
* **Grafik Türü:** Dikey Sütun Grafiği (Bar chart).
* **Başlık:** Taşıma Moduna Göre Ortalama Sevkiyat Ücreti
* **X Ekseni:** Taşıma Modu (Kara, Demiryolu, Deniz, Hava)
* **Y Ekseni:** Ortalama Ücret (TL)
* **Veri Değerleri:**
  * Kara: 4.476,02 TL
  * Demiryolu: 2.850,24 TL
  * Deniz: 1.823,49 TL
  * Hava: 14.028,00 TL
* **Özellikler:** Sütunların üzerinde Türk Lirası para birimi simgesi veya "TL" formatında biçimlendirilmiş veri etiketleri bulunmalı, eksen etiketlerinde birim açıkça belirtilmelidir.

## Görsel Tasarım İlkeleri

* **Çözünürlük:** 300 DPI, yüksek kaliteli PNG formatı.
* **Renk Paleti:**
  * Ana Renk (Primary): Lacivert / Koyu Mavi (`#1F4E79`)
  * Vurgu Renkleri: Mavi (`#2E75B6`), Çelik Mavisi (`#5B9BD5`), Turkuaz (`#41B6E6`)
  * Arka Plan: Beyaz (`#FFFFFF`), hafif gri ızgara çizgileri (`#E0E0E0`, alpha=0.6).
* **Tipografi:** Sans-serif (Segoe UI, Arial, DejaVu Sans), başlıklar 14-16pt kalın (bold), eksen etiketleri 11-12pt, veri etiketleri 10pt.
* **Marjinler:** Başlık ve etiketlerin kırpılmaması için `bbox_inches='tight'` ile kaydedilir.

## Çalıştırma Talimatı

Taslak onaylandıktan sonra grafikler aşağıdaki komutla üretilir:

```bash
python src/grafik_uret.py
```

## Bitiş ve Teslim Koşulları

1. `skills/fe-gorsel/SKILL.md` dosyası oluşturulmuş ve commit'lenmiş olmalıdır.
2. `visuals/zaman-serisi.png` ve `visuals/kirilim.png` üretilmiş olmalıdır.
3. Taslak ekran görüntüsü Issue #16'ya yüklenmiş olmalıdır.
4. Issue #16'ya aşağıdaki şablona uygun teslim yorumu bırakılmalıdır:
   > Grafikler hazır — commit `<hash>`. Dosyalar: visuals/zaman-serisi.png, visuals/kirilim.png. Veri: data/lojistik-sevkiyat.csv. Metrikler: docs/analiz-g1.md.
