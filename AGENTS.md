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
| pm-rapor | skills/pm-rapor/SKILL.md | İrem Deneri (PM) | Issue ve devir yorumlarından haftalık sprint raporunu üretir (reports/report-w03.md) | Ajana: "skills/pm-rapor/SKILL.md talimatını izleyerek raporu üret" |
| be-veri | skills/be-veri/SKILL.md | Ceren Gözel (BE) | Sabit tohumla tedarik verisini üretir (data/tedarik_siparisleri.csv, 240 satır, 10 alan) | `python src/veri_uret.py` |
| dq-analiz | skills/dq-analiz/SKILL.md | Serra Erdem (DQ) | Veriden 6 metrik hesaplar, yorum + 3 gözlem + 1 öneri yazar (docs/analiz-g1.md) | `python src/analiz_g1.py` |
| fe-gorsel | skills/fe-gorsel/SKILL.md | Baki Korkmaz (FE) | Hazır: CSV'den zaman serisi ve kırılım grafikleri üretir (visuals/) | `python src/grafik_uret.py` |
| dq-test | skills/dq-test/SKILL.md | Serra Erdem (DQ) | Veri için test senaryoları yazar (tests/test-cases.md); sonuçlar Hafta 4'te tests/test-log.md'ye işlenir | Skill adımlarını izle |

## Güncelleme kuralı
Yeni bir skill commit'lendiğinde ilgili satır güncellenir. Bu dosyadan PM sorumludur.
