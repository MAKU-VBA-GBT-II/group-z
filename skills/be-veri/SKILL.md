[SKILL (1).md](https://github.com/user-attachments/files/34037703/SKILL.1.md)
---
name: be-veri
description: Tedarik sektörü için sabit tohumlu (seed=42) sentetik sipariş verisi üretir (data/tedarik_siparisleri.csv, 240 satır, 10 alan) ve kabul kriterlerine göre doğrular. Veri üretimi, yeniden üretim veya CSV doğrulaması istendiğinde kullan (BE rolü).
---

# be-veri — Tedarik sentetik veri üretimi

## Ne yapar
`src/veri_uret.py` betiğini sabit tohumla çalıştırarak `data/tedarik_siparisleri.csv` dosyasını üretir, kabul kriterlerini doğrular ve DQ ile FE için devir teslim yorumunu hazırlar. Veri sentetiktir; gerçek kişi veya firma içermez.

## Kullanılan dosyalar
| Dosya | Rol |
|-------|-----|
| `src/veri_uret.py` | Üretim betiği (yalnızca Python standart kütüphanesi) |
| `data/tedarik_siparisleri.csv` | Çıktı: sentetik sipariş verisi |
| `src/analiz_g1.py` | Tüketici: DQ bu CSV'yi okuyarak metrik hesaplar |
| `src/grafik_uret.py` | Tüketici: FE bu CSV'den grafik üretir |

Şema değişirse tüketici betikler (`analiz_g1.py`, `grafik_uret.py`) bozulur; önce DQ ve FE ile alan listesi onaylanmalıdır.

## Şema (10 alan)
| Alan | Tip | Kural |
|------|-----|-------|
| `siparis_id` | metin | `SIP-0001` biçimi, benzersiz |
| `siparis_tarihi` | tarih | `YYYY-MM-DD`, 2026-01-03 ile 2026-09-29 arası |
| `tedarikci` | metin | 6 değer: Anadolu Tedarik A.Ş., Marmara Endüstri, Trakya Paketleme, Karadeniz Hammadde, Akdeniz Ticaret, Ege Lojistik Ltd. |
| `urun_kategorisi` | metin | 5 değer: Hammadde, Ambalaj, Yedek Parça, Elektronik, Kimyasal |
| `depo_bolgesi` | metin | 5 değer: Ege, Marmara, Akdeniz, Karadeniz, İç Anadolu |
| `miktar` | tam sayı | 15 ile 4849 arası |
| `birim_fiyat_tl` | ondalık | TL, 2 basamak |
| `toplam_tutar_tl` | ondalık | `miktar × birim_fiyat_tl`, 2 basamak |
| `teslim_suresi_gun` | tam sayı | 2 ile 18 arası |
| `teslimat_durumu` | metin | 3 değer: Zamanında, Gecikmiş, Kısmi Teslim |

## Çalıştırma
Repo kök dizininden:

```bash
python src/veri_uret.py
```

Varsayılan: `seed=42`, 240 satır. Çıktı her seferinde aynı dosyayı üretmelidir.

## Adım adım talimat
1. **Şemayı onaylat.** Yukarıdaki alan listesini DQ ile netleştir. Şema değişecekse önce bu dosyayı, sonra betiği güncelle.
2. **Betiği çalıştır.** `python src/veri_uret.py` ile `data/tedarik_siparisleri.csv` oluşur.
3. **Tekrarlanabilirliği doğrula.** Betiği iki kez çalıştırıp çıktıları karşılaştır; fark olmamalı:
   ```bash
   python src/veri_uret.py
   cp data/tedarik_siparisleri.csv /tmp/ilk.csv
   python src/veri_uret.py
   cmp /tmp/ilk.csv data/tedarik_siparisleri.csv && echo "AYNI"
   ```
   Betikte rastgelelik `random.seed(42)` ile sabitlenir; başka bir rastgelelik kaynağı (ör. `Faker`) kullanılırsa o da aynı tohumla başlatılmalıdır.
4. **Kabul kriterlerini kontrol et:**
   - en az 100 satır (şu an 240)
   - en az 6 alan (şu an 10)
   - ana kategorik alanda (`urun_kategorisi`) en az 4 farklı değer (şu an 5)
   - boş değer yok
   - `siparis_id` benzersiz
   - `toplam_tutar_tl = miktar × birim_fiyat_tl` (en fazla 0,01 TL fark)

   Hızlı kontrol:
   ```bash
   python3 - <<'PY'
   import csv
   s = list(csv.DictReader(open("data/tedarik_siparisleri.csv", encoding="utf-8-sig")))
   print("satir:", len(s), "| alan:", len(s[0]))
   print("kategori:", len({r["urun_kategorisi"] for r in s}))
   print("bos:", sum(v == "" for r in s for v in r.values()))
   print("id benzersiz:", len({r["siparis_id"] for r in s}) == len(s))
   print("tutar uyumsuz:", sum(abs(float(r["miktar"]) * float(r["birim_fiyat_tl"]) - float(r["toplam_tutar_tl"])) > 0.01 for r in s))
   PY
   ```
5. **Commit'le.** Betik, CSV ve bu skill ayrı ve anlamlı mesajlarla commit'lenir (ör. `feat(be): tedarik veri üreticisi ve CSV`).
6. **Devir teslim yorumu yaz.** DQ ve FE Issue'larına commit hash'iyle:
   > Veri hazır — commit `<hash>`. Dosya: `data/tedarik_siparisleri.csv` (240 satır, 10 alan). Yeniden üretmek için: `python src/veri_uret.py`.

   Bu yorum DQ ve FE'nin başlama iznidir.

## Notlar
- Parametre veya şema değiştirirsen CSV'yi yeniden üret ve devir yorumunu yeni hash ile güncelle.
- Yeni satır sayısı veya alan sayısı `AGENTS.md` ve devir yorumundaki değerlerle uyumlu olmalıdır.
