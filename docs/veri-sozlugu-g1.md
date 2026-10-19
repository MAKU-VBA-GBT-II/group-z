# Veri Sözlüğü — Görev 1 (Tedarik)

**Dosya:** `data/tedarik_siparisleri.csv` · **Üretici:** `src/veri_uret.py` (seed=42)
**Kodlama:** UTF-8, ayraç `,`, ondalık ayraç `.`, tarih biçimi `YYYY-MM-DD`
**Boyut:** 240 satır × 10 alan · **Dönem:** 2026-01-01 – 2026-09-30
**Birim kaydı:** Bir satır = bir tedarik siparişi (sentetik veri, gerçek kişi/firma değildir).

## Alanlar

| # | Alan | Tip | Açıklama | Geçerli değer / aralık |
|---|------|-----|----------|------------------------|
| 1 | `siparis_id` | metin | Benzersiz sipariş numarası | `SIP-0001` … `SIP-0240`, tarih sırasıyla artar |
| 2 | `siparis_tarihi` | tarih | Siparişin verildiği gün | 2026-01-01 – 2026-09-30 (hafta sonu nadir) |
| 3 | `tedarikci` | kategorik | Siparişin verildiği tedarikçi | 6 değer: Anadolu Tedarik A.Ş., Ege Lojistik Ltd., Marmara Endüstri, Akdeniz Ticaret, Karadeniz Hammadde, Trakya Paketleme |
| 4 | `urun_kategorisi` | kategorik (**ana**) | Sipariş edilen ürün grubu | 5 değer: Hammadde, Ambalaj, Elektronik, Kimyasal, Yedek Parça |
| 5 | `depo_bolgesi` | kategorik | Teslimatın yapıldığı depo bölgesi | 5 değer: Marmara, Ege, İç Anadolu, Akdeniz, Karadeniz |
| 6 | `miktar` | tam sayı | Sipariş edilen adet | ≥ 10 (kategoriye göre 10–5000) |
| 7 | `birim_fiyat_tl` | ondalık | Adet başına fiyat, **TL** | > 0, 2 ondalık |
| 8 | `toplam_tutar_tl` | ondalık | `miktar × birim_fiyat_tl`, **TL** | > 0, 2 ondalık |
| 9 | `teslim_suresi_gun` | tam sayı | Siparişten teslimata geçen süre, **gün** | 2 – 18 |
| 10 | `teslimat_durumu` | kategorik | Teslimatın sonucu | `Zamanında`, `Gecikmiş`, `Kısmi Teslim` |

## Kurallar ve notlar

- **Boş (eksik) değer yoktur.** Tüm alanlar her satırda doludur.
- **Tutarlılık:** `toplam_tutar_tl = miktar × birim_fiyat_tl` (yuvarlama farkı ≤ 0,01).
- **Gecikme:** `Gecikmiş` siparişlerin `teslim_suresi_gun` değerine 3–8 gün eklenmiştir; bu yüzden genelde en uzun süreler bu grupta çıkar.
- **Mevsimsellik:** Sipariş sayısı aylara göre değişir: en yoğun dönem Nisan–Haziran (38, 33 ve 36 sipariş), en sakin ay Ağustos (16 sipariş); Eylül'de (29) toparlanma görülür. Zaman serisi grafiğinde bu desen görünür.
- **Tedarikçi farkı:** Her tedarikçinin gecikme olasılığı ve fiyat düzeyi farklıdır (örn. Akdeniz Ticaret en çok gecikme, en düşük fiyat).
- **Tekrarlanabilirlik:** `python src/veri_uret.py` (seed=42) her çalıştırmada birebir aynı dosyayı üretir.

## Analiz ve görselleştirme için önerilen eksenler

- **Zaman serisi:** `siparis_tarihi` (aylık) → sipariş sayısı veya `toplam_tutar_tl` toplamı
- **Kırılım:** `urun_kategorisi` veya `tedarikci` → toplam tutar / ortalama teslim süresi / gecikme oranı
