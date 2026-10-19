# Test Senaryoları — Görev 1 (Tedarik)

**Hazırlayan:** Serra Erdem (DQ) · **Test edilen dosya:** `data/tedarik_siparisleri.csv` · **Şema:** `docs/veri-sozlugu-g1.md`

"Gerçekleşen sonuç" sütunu Hafta 4'te doldurulacaktır.

| No | Kategori | Senaryo | Beklenen sonuç | Gerçekleşen sonuç |
|----|----------|---------|----------------|-------------------|
| T1 | Dosya var mı | `data/tedarik_siparisleri.csv` repoda mevcut ve UTF-8 olarak açılabiliyor mu? | Dosya vardır, hata vermeden okunur, ayraç `,` ve ondalık ayraç `.` | |
| T2 | Satır sayısı | Başlık satırı hariç kayıt sayısı sayılır. | 240 satır; `siparis_id` değerleri benzersiz, `SIP-0001` … `SIP-0240` | |
| T3 | Sütunlar | Başlık satırı kontrol edilir. | 10 sütun, bu sırayla: `siparis_id, siparis_tarihi, tedarikci, urun_kategorisi, depo_bolgesi, miktar, birim_fiyat_tl, toplam_tutar_tl, teslim_suresi_gun, teslimat_durumu` | |
| T4 | Tipler / aralıklar | `siparis_tarihi` biçimi ve aralığı kontrol edilir. | Tüm değerler `YYYY-MM-DD` biçiminde ve 2026-01-01 – 2026-09-30 arasında | |
| T5 | Tipler / aralıklar | `miktar`, `birim_fiyat_tl`, `teslim_suresi_gun` kontrol edilir. | `miktar` tam sayı ve ≥ 10; `birim_fiyat_tl` > 0 (2 ondalık); `teslim_suresi_gun` tam sayı ve 2–18 arası | |
| T6 | Tipler / tutarlılık | Her satırda `toplam_tutar_tl = miktar × birim_fiyat_tl` kontrol edilir; boş değer aranır. | Fark ≤ 0,01 TL; hiçbir alanda boş (eksik) değer yok | |
| T7 | Kategori değerleri | `tedarikci`, `urun_kategorisi`, `depo_bolgesi`, `teslimat_durumu` benzersiz değerleri listelenir. | `tedarikci` 6 değer; `urun_kategorisi` 5 değer (Hammadde, Ambalaj, Elektronik, Kimyasal, Yedek Parça); `depo_bolgesi` 5 değer (Marmara, Ege, İç Anadolu, Akdeniz, Karadeniz); `teslimat_durumu` yalnızca Zamanında, Gecikmiş, Kısmi Teslim | |
