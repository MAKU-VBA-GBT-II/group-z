# Hafta 3 Sprint Raporu — Grup Z (Tedarik)

**Hazırlayan:** İrem Deneri (PM) · **Üretim:** `skills/pm-rapor/SKILL.md` talimatıyla · **Son tarih:** 20 Ekim Salı 23:59

## Planlanan
| Issue | Başlık | Sorumlu | Son tarih |
|---|---|---|---|
| #7 | G1-veri | Ceren Gözel (BE) | 19 Ekim 22:00 |
| #8 | G1-analiz | Serra Erdem (DQ) | 20 Ekim 18:00 |
| #9 | G1-gorsel | Baki Korkmaz (FE) | 20 Ekim 18:00 |
| #10 | G1-test | Serra Erdem (DQ) | 20 Ekim 22:00 |

Ek olarak her üye kendi skill'ini yazacak; PM `AGENTS.md` envanterini ve bu raporu hazırlayacaktı.

## Yapılan
- **G1-veri (#7):** `src/veri_uret.py`, `data/tedarik_siparisleri.csv` (240 satır, 10 alan, 5 kategori), `docs/veri-sozlugu-g1.md`, `skills/be-veri/SKILL.md` — commit `19df2d1` (18 Ekim).
- **G1-analiz (#8):** `docs/analiz-g1.md` (6 metrik, 3 gözlem, 1 öneri), `src/analiz_g1.py` — commit `22b085c` (19 Ekim); `skills/dq-analiz/SKILL.md` — `2ce5d2a`.
- **G1-test (#10):** `tests/test-cases.md` (7 senaryo) — commit `140d6df` (19 Ekim); `skills/dq-test/SKILL.md` — `e1eac99`.
- **PM:** 4 Issue, "Görev 1 Panosu", `AGENTS.md`, `skills/pm-rapor/SKILL.md`.

## Tıkanan / sorunlu
1. **G1-gorsel (#9):** İlk teslimdeki (20 Ekim) iki grafik BE verisinden üretilmemişti (örnek değerler: A/B/C pastası, 4 noktalı seri). Düzeltme (#13): `src/grafik_uret.py` ile CSV'den yeniden üretim ve yeniden yazılan `fe-gorsel` skill'i. Bu iş bitene kadar `AGENTS.md`'de FE satırı **Eksik** olarak işaretlidir.
2. **Devir yorumları:** Issue'lara "hazır — commit" yorumları geç veya eksik düştü; FE kartına devir (G1-veri → G1-gorsel, G1-analiz → G1-gorsel) yorumları sonradan eklendi.
3. **Devir eksikleri:** Ceren ve Serra'nın devir yorumları #9'a (FE kartı) yazılmadı; Baki veri ve analiz hazır olmadan grafik yaptı. Yorumlar istendi.
4. **Skill'ler:** `fe-gorsel` başlangıçta iki satırdı; `dq-test` biçimi bozuktu (kaçışlı `\---`); `AGENTS.md` içinde yanlış dosya adı (`tedarik-verisi.csv`) ve "(Tamamlandı)" yer tutucuları vardı — düzeltildi.
5. **Pano:** Kartlar yalnız Backlog→Done olarak taşındı; In progress aşaması kullanılmadı.

## Kim ne yaptı
| Kişi | Rol | Teslim |
|---|---|---|
| Ceren Gözel | BE | Veri betiği, CSV, veri sözlüğü, be-veri skill'i |
| Serra Erdem | DQ | Analiz (6 metrik), 7 test senaryosu, dq-analiz ve dq-test skill'leri |
| Baki Korkmaz | FE | Grafik taslakları ve ilk PNG'ler (düzeltilmesi gerekti), fe-gorsel skill'i taslağı |
| İrem Deneri | PM | Issue/pano yönetimi, AGENTS.md, pm-rapor skill'i, bu rapor, düzeltme koordinasyonu |

## Sonraki adım (Hafta 4)
`tests/test-log.md` içinde test senaryoları çalıştırılıp "gerçekleşen sonuç" doldurulacak.
