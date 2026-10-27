---
name: pm-rapor
description: Grup Z'nin haftalık sprint raporunu (reports/report-wNN.md) GitHub Issue, pano ve commit verisinden, sabit şablonla ve kanıt linkleriyle üretir.
---

# pm-rapor

## Ne yapar
Görev 1 Issue'larını (G1-veri, G1-analiz, G1-gorsel, G1-test), devir yorumlarını ve repodaki dosyaları denetleyip haftalık sprint raporunu `reports/report-wNN.md` olarak üretir (NN = hafta numarası, örn. `w03`, `w04`). Her iddia bir commit hash'i veya Issue yorum linkiyle desteklenir.

## Ekip ve Issue eşleşmesi
| Rol | Kişi | GitHub | Issue | Teslim | Skill |
|---|---|---|---|---|---|
| PM | İrem Deneri | Irem-Deneri | — | Issue/pano, AGENTS.md, rapor | `skills/pm-rapor/SKILL.md` |
| BE | Ceren Gözel | cerengzell | #7 G1-veri | `src/veri_uret.py`, `data/tedarik_siparisleri.csv`, `docs/veri-sozlugu-g1.md` | `skills/be-veri/SKILL.md` |
| DQ | Serra Erdem | serraerdem22-droid | #8 G1-analiz, #10 G1-test | `docs/analiz-g1.md`, `src/analiz_g1.py`, `tests/test-cases.md` | `skills/dq-analiz/SKILL.md`, `skills/dq-test/SKILL.md` |
| FE | Baki Korkmaz | bakikorkmaz | #9 G1-gorsel | `visuals/zaman_serisi.png`, `visuals/kirilim.png`, `src/grafik_uret.py` | `skills/fe-gorsel/SKILL.md` |

## Adım adım talimat
1. **Hafta numarasını belirle.** İstekte verilen NN değerini kullan (örn. 04). Çıktı: `reports/report-wNN.md`.
2. **Issue durumunu oku.** #7–#10 ve açık Hata/Geliştirme Issue'ları için başlık, sorumlu, son tarih, durum (açık/kapalı) ve pano sütununu listele.
3. **Devir zincirini denetle.** Her Issue'da şu yorumları ara ve hash/link olarak kaydet:
   - G1-analiz ve G1-gorsel: "Veri hazır — commit `<hash>`" (BE)
   - G1-gorsel: "Analiz hazır — commit `<hash>`" (DQ)
   - G1-test: "Test senaryoları hazır — commit `<hash>`" (DQ)
   - G1-gorsel: "Görseller hazır — commit `<hash>`" (FE)
   Eksik yorum varsa "Tıkanan" bölümüne yaz.
4. **Dosyaları doğrula.** Her dosyanın hem var olduğunu hem de boş olmadığını (boyut > 0 bayt, örn. `ls -lh`) kontrol et, ayrıca içerik kriterini denetle:
   - `data/tedarik_siparisleri.csv` (≥100 satır, ≥6 alan)
   - `docs/veri-sozlugu-g1.md`, `docs/analiz-g1.md`
   - `visuals/zaman_serisi.png` ve `visuals/kirilim.png` (tam bu adlarla, ikisi de > 0 bayt)
   - `tests/test-cases.md` (≥5 senaryo)
   - her rol için `skills/<rol>-<iş>/SKILL.md`, kökte `AGENTS.md`
5. **Raporu şablonla derle** (aşağıdaki başlıklar, bu sırayla). "Kim ne yaptı" ve "Yapılan" satırlarına commit hash'i veya Issue yorum linki ekle.
6. **Commit'le.** Dosyayı `reports/report-wNN.md` olarak commit'le; mesaja ilgili Issue numarasını yaz (örn. `Fixes #11`).

## Rapor şablonu
```
# Hafta NN Sprint Raporu — Grup Z (Tedarik)
**Hazırlayan:** <PM> · **Üretim:** skills/pm-rapor/SKILL.md · **Son tarih:** <tarih>
## Planlanan        (tablo: Issue | Başlık | Sorumlu | Son tarih)
## Yapılan          (Issue başına dosya + commit hash'i)
## Tıkanan / sorunlu (eksik devir, gecikme, hata Issue'ları; nedeniyle)
## Kim ne yaptı     (kişi | rol | teslim + hash/link)
## Sonraki adım
```

## Kullandığı dosyalar
- Girdi: GitHub Issue'ları (#7–#10 ve Hata/Geliştirme Issue'ları), "Görev 1 Panosu", `AGENTS.md`, `data/`, `docs/`, `visuals/`, `tests/`, `skills/`
- Çıktı: `reports/report-wNN.md`

## Nasıl çalıştırılır
Bir yapay zekâ ajanına (Claude, Codex vb.) şu istem verilir:
> "skills/pm-rapor/SKILL.md talimatını izleyerek bu haftanın raporunu reports/report-w04.md olarak üret. Hafta numarası: 04."
Ajan Issue ve repo durumunu okur, raporu şablona göre yazar; PM çıktıyı commit'ler.
