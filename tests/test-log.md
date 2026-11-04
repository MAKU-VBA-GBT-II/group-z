# Test Log — Grup Z (Hafta 4)

Çalıştırma: 27.10.2026
Komut (repo kökünden): `python tests/test_calistir.py` (test-cases.md'deki T1–T7 kontrolleri)
Veri dosyası: `data/tedarik_siparisleri.csv` — son değiştiren commit `1745296`, 240 satır × 10 sütun

| No | Senaryo | Beklenen | Gerçekleşen | Sonuç |
|----|---------|----------|-------------|-------|
| T1 | Dosya okunabiliyor mu | data/tedarik_siparisleri.csv açılır | Dosya açıldı, 240 kayıt satırı okundu | GEÇTİ |
| T2 | Satır sayısı | 240 satır, SIP-0001…SIP-0240 benzersiz | 240 satır, 240 benzersiz siparis_id | GEÇTİ |
| T3 | Sütun şeması | 10 sütun (siparis_id … teslimat_durumu) | 10 sütun, sıra beklenenle aynı | GEÇTİ |
| T4 | Tarih biçimi/aralığı | YYYY-MM-DD, 2026-01-01…2026-09-30 | Aralık 2026-01-03 – 2026-09-29 | GEÇTİ |
| T5 | Tip ve aralıklar | miktar ≥ 10, birim_fiyat > 0, teslim_suresi_gun 2-18 | Üç kural da sağlanıyor | GEÇTİ |
| T6 | Tutarlılık | toplam_tutar_tl = miktar × birim_fiyat_tl | En büyük fark 0,0000 TL; boş değer 0 | GEÇTİ |
| T7 | Kategori değerleri | 6 tedarikçi, 5 kategori, 5 bölge, 3 teslimat durumu | 6 / 5 / 5 / 3 | GEÇTİ |

## Not
İlk çalıştırmada (commit a48e86a sonrası) `data/tedarik_siparisleri.csv` 4 satırlık,
3 sütunlu bir dosyayla değiştirilmişti (commit e08f9bb) ve T2–T7 KALDI. Dosya
27.10.2026 21:46'da orijinal 240 satırlık haliyle geri yüklendi (commit 1745296);
bu günlükteki sonuçlar geri yüklenen dosyayla elde edilmiştir.
