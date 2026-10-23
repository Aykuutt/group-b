---
name: be-veri
description: Grup B'nin sentetik sevkiyat verisini src/uret_sevkiyat.py ile üretir. Veri üretimi yapılacağı zaman kullan.
---

# be-veri — Sentetik sevkiyat verisi üretimi

**Ne yapar:** Lojistik için sabit tohumlu (42) sevkiyat verisi üretir. Aynı tohum her zaman aynı dosyayı verir. Gerçek kişi veya firma verisi yoktur.

## Girdiler
- Depo: MAKU-VBA-GBT-II/group-b
- Issue: G1-veri (#14)
- Tohum: 42, hedef 300 satır
- Şema: docs/veri-sozlugu-g1.md

## Adımlar
1. Şemayı DQ ile Issue yorumlarında kesinleştir.
2. Çalıştır: `python src/uret_sevkiyat.py`
3. Kontrol et: en az 100 satır, en az 6 alan, tasima_modu'nda en az 4 değer, ikinci çalıştırmada aynı dosya.
4. docs/veri-sozlugu-g1.md güncel mi bak.
5. Commit ve push yap, G1-analiz ve G1-gorsel Issue'larına devir yorumu bırak.

## Devir yorumu şablonu
Veri hazır — commit HASH. Dosya: data/lojistik-sevkiyat.csv, 300 satır, 10 alan. Şema: docs/veri-sozlugu-g1.md. Tohum: 42. Çalıştırma: python src/uret_sevkiyat.py.

## Kullanılan dosyalar
- Okur: Issue yorumları (DQ ile şema kararı)
- Yazar: src/uret_sevkiyat.py, data/lojistik-sevkiyat.csv, docs/veri-sozlugu-g1.md

## Nasıl çalıştırılır
Ajana (Claude Code, Codex vb.): "be-veri skill'ini kullanarak src/uret_sevkiyat.py'yi çalıştır ve veriyi üret." Elle: `python src/uret_sevkiyat.py`
