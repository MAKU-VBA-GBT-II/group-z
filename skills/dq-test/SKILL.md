---
name: dq-test
description: Tedarik veri dosyası için en az 5 test senaryosu yazar, tests/test_calistir.py ile çalıştırır ve sonuçları tests/test-log.md dosyasına işler.
---

# dq-test

## Ne yapar
`docs/veri-sozlugu-g1.md` şemasındaki kurallardan test senaryoları çıkarır
(`tests/test-cases.md`), bunları `data/tedarik_siparisleri.csv` üzerinde çalıştırır
ve sonucu `tests/test-log.md` dosyasına yazar. Bir senaryo kalırsa hata Issue'su açılır.

## Kullandığı dosyalar
| Dosya | Rol |
|---|---|
| `data/tedarik_siparisleri.csv` | Girdi (BE) |
| `docs/veri-sozlugu-g1.md` | Girdi: şema kuralları |
| `tests/test-cases.md` | Çıktı: senaryolar (T1–T7) |
| `tests/test_calistir.py` | Betik: T1–T7 kontrollerini çalıştırır |
| `tests/test-log.md` | Çıktı: beklenen / gerçekleşen / sonuç |

## Nasıl çalıştırılır
Repo kök dizininden:

```bash
python tests/test_calistir.py
```

## Adım adım talimat
1. `G1-veri` Issue'sunda "Veri hazır — commit ..." yorumunu bekle.
2. Şema kurallarından en az 5 senaryo çıkar ve `tests/test-cases.md` dosyasına yaz.
3. Betiği çalıştır; her senaryo için GEÇTİ veya KALDI çıktısı alınır.
4. Sonuçları `tests/test-log.md` tablosuna işle (beklenen, gerçekleşen, sonuç).
5. Kalan senaryo varsa hata Issue'su aç ve BE'ye bildir; düzeltmeden sonra testi yeniden çalıştır.
6. `G1-test` Issue'suna yaz: "Test senaryoları hazır — commit `<hash>`".
