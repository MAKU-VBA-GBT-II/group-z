# Veri Sözlüğü: Tedarik (Görev 2)

**Sektör:** Tedarik (sentetik sipariş verisi, gerçek kişi/firma değildir)
**Dosya:** `data/tedarik_siparisleri.csv` · **Üretici:** `src/veri_uret.py` (seed=42)
**Hedeflenen satır sayısı:** 240 (başlık hariç) · **Alan sayısı:** 10
**Kodlama:** UTF-8, ayraç `,`, ondalık ayraç `.`, tarih biçimi `YYYY-MM-DD`
**Dönem:** 2026-01-01 – 2026-09-30
**Birim kaydı:** Bir satır = bir tedarik siparişi

## 1. Alanlar

| # | Alan adı | Tip | Aralık / kural | Örnek değer |
|---|----------|-----|----------------|-------------|
| 1 | `siparis_id` | metin | Benzersiz; `SIP-0001` … `SIP-0240`, tarih sırasıyla artar | SIP-0001 |
| 2 | `siparis_tarihi` | tarih | 2026-01-01 – 2026-09-30, `YYYY-MM-DD` (hafta sonu nadir) | 2026-01-05 |
| 3 | `tedarikci` | kategorik | 6 değerden biri: Anadolu Tedarik A.Ş., Ege Lojistik Ltd., Marmara Endüstri, Akdeniz Ticaret, Karadeniz Hammadde, Trakya Paketleme | Ege Lojistik Ltd. |
| 4 | `urun_kategorisi` | kategorik | 5 değerden biri: Hammadde, Ambalaj, Elektronik, Kimyasal, Yedek Parça | Ambalaj |
| 5 | `depo_bolgesi` | kategorik | 5 değerden biri: Marmara, Ege, İç Anadolu, Akdeniz, Karadeniz | Ege |
| 6 | `miktar` | tam sayı | ≥ 10 (kategoriye göre 10–5000) | 400 |
| 7 | `birim_fiyat_tl` | ondalık | > 0, 2 ondalık, birim: TL | 12.50 |
| 8 | `toplam_tutar_tl` | ondalık | `miktar × birim_fiyat_tl` (fark ≤ 0,01), > 0, 2 ondalık, birim: TL | 5000.00 |
| 9 | `teslim_suresi_gun` | tam sayı | 2 – 18, birim: gün | 6 |
| 10 | `teslimat_durumu` | kategorik | `Zamanında`, `Gecikmiş`, `Kısmi Teslim` | Zamanında |

## 2. Genel kurallar

- Boş (eksik) değer yoktur; tüm alanlar her satırda doludur.
- `toplam_tutar_tl = miktar × birim_fiyat_tl` her satırda geçerlidir.
- `Gecikmiş` siparişlerin teslim süresine 3–8 gün eklenmiştir.
- Sipariş sayısı mevsimseldir: Nisan–Haziran yoğun, Ağustos en sakin ay.
- Her tedarikçinin gecikme olasılığı ve fiyat düzeyi farklıdır.
- `python src/veri_uret.py` (seed=42) her çalıştırmada aynı dosyayı üretir.

## 3. Analiz metrikleri

| # | Metrik adı | Formül | Neyi ölçer |
|---|------------|--------|------------|
| M1 | Toplam harcama (TL) | `SUM(toplam_tutar_tl)` | Dönem boyunca tedarike harcanan toplam bütçe |
| M2 | Ortalama teslim süresi (gün) | `AVG(teslim_suresi_gun)` | Tedarik sürecinin ortalama hızı |
| M3 | Kategori bazında toplam harcama (kırılım 1) | `SUM(toplam_tutar_tl)` `GROUP BY urun_kategorisi` | Bütçenin hangi ürün gruplarına gittiği |
| M4 | Aylık sipariş sayısı ve harcama (kırılım 2, zaman) | `COUNT(siparis_id)` ve `SUM(toplam_tutar_tl)` `GROUP BY ay(siparis_tarihi)` | Siparişlerin mevsimsel/zamansal seyri |
| M5 | En çok harcama yapılan ilk 3 tedarikçi (top-N) | `SUM(toplam_tutar_tl)` `GROUP BY tedarikci` `ORDER BY` toplam `DESC` `LIMIT 3` | Hangi tedarikçilere bütçenin en büyük payının gittiği |

**Ek metrik (isteğe bağlı):** Tedarikçi bazında gecikme oranı = `COUNT(teslimat_durumu = 'Gecikmiş') / COUNT(*) × 100`, `GROUP BY tedarikci`.