---
name: fe-gorsel
description: BE'nin tedarik CSV'sinden iki grafik üretir (aylık tutar zaman serisi + kategori kırılımı) ve visuals/ altına PNG olarak yazar. FE adımı.
---

# fe-gorsel — Tedarik görselleştirme

## Ne yapar
`src/grafik_uret.py` betiği `data/tedarik_siparisleri.csv` dosyasını okur ve iki grafik üretir: aylık toplam sipariş tutarı (zaman serisi) ve ürün kategorisine göre toplam tutar (kırılım). Grafikler yalnızca CSV'den hesaplanır; elle yazılmış veri kullanılmaz.

## Kullandığı dosyalar
| Dosya | Rol |
|-------|-----|
| `data/tedarik_siparisleri.csv` | Girdi (BE) |
| `docs/analiz-g1.md` | Kontrol: grafikteki değerler M3/M6 ile tutmalı (DQ) |
| `src/grafik_uret.py` | Üretim betiği (matplotlib) |
| `visuals/zaman_serisi.png`, `visuals/kirilim.png` | Çıktı |

## Nasıl çalıştırılır
Repo kök dizininden:

```bash
pip install matplotlib
python src/grafik_uret.py
```

## Adım adım talimat
1. `G1-veri` Issue'sunda "Veri hazır — commit ..." yorumunu bekle.
2. Betiği çalıştır; iki PNG `visuals/` altına yazılır.
3. Kontrol: her grafikte başlık, eksen etiketi ve birim (milyon TL) var; kategori payları analizdeki M3 ile aynı (Elektronik %32,9, Hammadde %29,4 ...).
4. Betiği ve PNG'leri commit'le (örn. `feat(fe): CSV'den üretilen grafikler`).
5. `G1-gorsel` Issue'suna yaz: "Görseller hazır — commit `<hash>`".
