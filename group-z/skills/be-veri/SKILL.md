---
name: be-veri
description: Tedarik sektörü için sentetik sipariş verisi (CSV) üretir ve veri sözlüğüyle birlikte teslim eder. BE (Backend / Veri Üretici) adımı.
---

# be-veri — Tedarik sentetik veri üretimi

## Ne yapar
Sabit tohumlu `src/veri_uret.py` betiğini çalıştırarak `data/tedarik_siparisleri.csv` dosyasını (240 satır, 10 alan) üretir; şemayı `docs/veri-sozlugu-g1.md` ile uyumlu tutar ve DQ/FE'ye devir teslim yorumunu hazırlar.

## Kullandığı dosyalar
| Dosya | Rol |
|-------|-----|
| `src/veri_uret.py` | Üretim betiği (yalnızca Python standart kütüphanesi) |
| `data/tedarik_siparisleri.csv` | Çıktı: sentetik sipariş verisi |
| `docs/veri-sozlugu-g1.md` | Şema: alan adı, tip, aralık, kurallar |

## Nasıl çalıştırılır
Repo kök dizininden:

```bash
python src/veri_uret.py                      # varsayılan: seed=42, 240 satır
python src/veri_uret.py --seed 42 --satir 300  # parametreli
```

## Adım adım talimat
1. **Şemayı kesinleştir.** DQ ile alan listesini onaylat (`docs/veri-sozlugu-g1.md`). Şema değişirse önce sözlüğü, sonra betiği güncelle.
2. **Betiği çalıştır.** Yukarıdaki komutu kök dizinden çalıştır; `data/tedarik_siparisleri.csv` oluşur.
3. **Tekrarlanabilirliği doğrula.** Betiği iki kez çalıştır; iki çıktı `cmp`/`diff` ile birebir aynı olmalı.
4. **Kabul kriterlerini kontrol et:**
   - en az 100 satır (şu an 240)
   - en az 6 alan (şu an 10)
   - ana kategorik alanda (`urun_kategorisi`) en az 4 farklı değer (şu an 5)
   - boş değer yok; `toplam_tutar_tl = miktar × birim_fiyat_tl`
5. **Commit'le.** Betik, CSV, veri sözlüğü ve bu skill ayrı/anlamlı mesajlarla commit'lenir (örn. `feat(be): tedarik veri üreticisi ve CSV`).
6. **Devir teslim yorumu yaz.** `G1-analiz` ve `G1-gorsel` Issue'larına, commit hash'iyle:
   > Veri hazır — commit `<hash>`. Dosya: `data/tedarik_siparisleri.csv` (240 satır, 10 alan). Şema: `docs/veri-sozlugu-g1.md`. Yeniden üretmek için: `python src/veri_uret.py`.
   Bu yorum DQ ve FE'nin başlama iznidir.

## Notlar
- Veri sentetiktir; gerçek kişi veya firma içermez.
- Parametre/şema değişikliği yaparsan CSV'yi yeniden üretip devir yorumunu yeni hash ile güncelle.
