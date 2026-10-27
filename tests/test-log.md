# Test Log — Grup Z (Hafta 4)

Çalıştırma: 27.10.2026, yerel klon (commit a48e86a)
Komut: `python test_calistir.py` (test-cases.md'deki T1-T7 kontrolleri)
Veri dosyası: data/tedarik_siparisleri.csv (son değiştiren commit: e08f9bb)

| No | Senaryo | Beklenen | Gerçekleşen | Sonuç |
|----|---------|----------|-------------|-------|
| T1 | Dosya okunabiliyor mu | data/tedarik_siparisleri.csv açılır | Dosya açıldı, 4 kayıt satırı okundu | GEÇTİ |
| T2 | Satır sayısı | 240 satır, SIP-0001…SIP-0240 benzersiz | 4 satır, siparis_id sütunu yok | KALDI |
| T3 | Sütun şeması | 10 sütun (siparis_id … teslimat_durumu) | 3 sütun: siparis_tarihi, urun_kategorisi, toplam_tutar_tl | KALDI |
| T4 | Tarih biçimi/aralığı | YYYY-MM-DD, 2026-01-01…2026-09-30 | Şema uyuşmadığı için doğrulanamadı | KALDI |
| T5 | Tip ve aralıklar | miktar ≥ 10, birim_fiyat > 0, teslim_suresi_gun 2-18 | İlgili sütunlar dosyada yok | KALDI |
| T6 | Tutarlılık | toplam_tutar_tl = miktar × birim_fiyat_tl | miktar ve birim_fiyat_tl sütunları yok | KALDI |
| T7 | Kategori değerleri | 6 tedarikçi, 5 kategori, 5 bölge, 3 teslimat durumu | Sadece urun_kategorisi var: Elektronik, Giyim, Ev | KALDI |

## Not
T2-T7'nin kalma sebebi tek: repodaki veri dosyası, test senaryolarının yazıldığı
veri setiyle aynı değil. Ayrıntı ve öneri için açılan Hata Issue'suna bakınız.
