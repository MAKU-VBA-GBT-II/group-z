---
name: dq-analiz
description: Tedarik sipariş verisinden 6 metrik hesaplar ve docs/analiz-g1.md dosyasını üretir.
---

# dq-analiz

## Ne yapar
`src/analiz_g1.py` betiği `data/tedarik_siparisleri.csv` dosyasından altı metrik hesaplar:
toplam tutar (M1), ortalama teslim süresi (M2), kategori kırılımı (M3), tedarikçi gecikme
oranı (M4), ilk 3 tedarikçi (M5) ve aylık sipariş sayısı (M6). Sonuçlar
`docs/analiz-g1.md` dosyasına, her metrik için yorum, 3 gözlem ve 1 eylem önerisiyle yazılır.

## Kullandığı dosyalar
| Dosya | Rol |
|---|---|
| `data/tedarik_siparisleri.csv` | Girdi (BE) |
| `docs/veri-sozlugu-g1.md` | Girdi: şema |
| `src/analiz_g1.py` | Betik: metrikleri hesaplar, `analiz_ciktisi.txt` üretir |
| `docs/analiz-g1.md` | Çıktı: yorumlu analiz belgesi |

## Nasıl çalıştırılır
Repo kök dizininden:

```bash
python src/analiz_g1.py
```

## Adım adım talimat
1. `G1-veri` Issue'sunda "Veri hazır — commit ..." yorumunu bekle; veri
