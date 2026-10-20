# AGENTS.md — Skill Envanteri (Grup Z)

Bu dosya, depodaki skill'lerin envanteridir: hangi skill nerede, ne işe yarar, nasıl kullanılır. Skill'ler eklendikçe güncellenir. Ajan araçları (Codex, Claude Code vb.) bu dosyayı otomatik okur.

## Proje
- Grup: Z
- Sektör: Tedarik
- Görev 1: Sektörde Mini Veri Hattı (BE → DQ → FE → DQ → PM)
- Teslim zinciri: her devir, ilgili Issue'ya yorumla kanıtlanır.

## Skill'ler

| Skill | Yol | Sahibi | Ne işe yarar | Nasıl kullanılır |
|-------|-----|--------|--------------|------------------|
| pm-rapor | skills/pm-rapor/SKILL.md | İrem Deneri (PM) | Issue ve devir yorumlarından haftalık sprint raporunu (reports/report-w03.md) üretir | Ajana: "skills/pm-rapor/SKILL.md talimatını izleyerek raporu üret" |
| be-veri | skills/be-veri/SKILL.md | Ceren Gözel (BE) | (Tamamlandı) Sabit tohumla tedarik verisi üretir (data/tedarik-verisi.csv) | (Tamamlandı) |
| dq-analiz | skills/dq-analiz/SKILL.md | Serra Erdem (DQ) | (Tamamlandı) Veriden 5 metrik çıkarır (docs/analiz-g1.md) | (bekleniyor) |
| fe-gorsel | skills/fe-gorsel/SKILL.md | Baki Korkmaz (FE) | (bekleniyor) Zaman serisi ve kırılım grafiklerini üretir (visuals/) | (bekleniyor) |
| dq-test | skills/dq-test/SKILL.md | Serra Erdem (DQ) | (Tamamlandı) Veri için test senaryoları yazar (tests/test-cases.md) | (Tamamlandı) |

## Güncelleme kuralı
Yeni bir skill commit'lendiğinde ilgili satırın "(bekleniyor)" kısımları doldurulur. Bu dosyadan PM sorumludur.
