# AGENTS.md GRUP-B Logistics Intelligence Network(LIN) SKİLL Envanteri

Bu repo, Şirket B (Lojistik) için sentetik sevkiyat veri hattı içerir.
Ajan, görev aldığında ilgili `SKILL.md` dosyasını okuyup talimatları izlemelidir.

| Skill | Konum | Sahibi | Ne işe yarar | Nasıl kullanılır |
|---|---|---|---|---|
| be-veri | `skills/be-veri/SKILL.md` | BE | Sabit tohumla 300 satırlık sevkiyat verisi üretir | `python src/veri_uret.py` |
| dq-analiz | `skills/dq-analiz/SKILL.md` | DQ | Teslimat süresi, gecikme oranı, rota tablosu, haftalık hacim, top-3 rota metriklerini hesaplar | `python src/analiz.py` (BE devir teslimi sonrası) |
| fe-gorsel | `skills/fe-gorsel/SKILL.md` | FE | Haftalık hacim ve rota yoğunluğu grafiklerini üretir | `python src/grafik_uret.py` (taslak Issue'ya eklendikten sonra) |
| pm-rapor | `skills/pm-rapor/SKILL.md` | Sude ÇUKURTAŞ PM | Haftalık raporu commit/Issue geçmişinden hazırlar | Ajana: "pm-rapor skill'ini oku" |
| dq-test | `skills/dq-test/SKILL.md` | DQ | Sevkiyat verisi için en az 5 manuel test senaryosu tanımlar; gerçekleşen sonuç alanlarını boş bırakır | Görev #17 için önce bu dosyayı oku; senaryoları `tests/test-cases.md` içine yaz |

## Devir teslim zinciri
BE veri → DQ analiz → FE görsel → DQ test → PM rapor.
Her adım ilgili Issue'ya commit hash'li yorumla biter.
> Kural: Roller görevden göreve döner (plan §1.3); skill'ler rolle birlikte el değiştirir. Yeni sahibi skill'i günceller ve bu tablodaki "Sahibi" sütununu değiştirir.
## Kurallar
- Veri sentetiktir; gerçek kişi verisi yok.
- Veri üretimi tohum 42 ile tekrarlanabilir.
- Yeni skill eklenince bu dosya güncellenir.
- "GitHub'da yoksa, yapılmamıştır": her iş bir Issue'ya bağlıdır; bitince Issue'ya kanıt yorumu (commit hash + dosya) yazılır.
- Gerçek kişi verisi asla depoya girmez; tüm veriler simülasyon ürünüdür.
- Veri üretimi sabit tohumla tekrarlanabilir olmalıdır.
- Hafta 5'ten itibaren `main`'e yalnızca PR ile girilir; kod/veri PR'ları DQ onayı olmadan merge edilmez.
