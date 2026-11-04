"""dq-test: tests/test-cases.md icindeki T1-T7 kontrollerini calistirir.
Calistirma (repo kokunden): python tests/test_calistir.py
"""
import csv
import sys
from datetime import date

YOL = "data/tedarik_siparisleri.csv"
SUTUNLAR = ["siparis_id", "siparis_tarihi", "tedarikci", "urun_kategorisi",
            "depo_bolgesi", "miktar", "birim_fiyat_tl", "toplam_tutar_tl",
            "teslim_suresi_gun", "teslimat_durumu"]
sonuclar = []


def kayit(no, gecti, aciklama):
    sonuclar.append(gecti)
    print(f"{no} | {'GECTI' if gecti else 'KALDI'} | {aciklama}")


try:
    with open(YOL, encoding="utf-8", newline="") as f:
        satirlar = list(csv.DictReader(f))
    kayit("T1", True, f"dosya acildi, {len(satirlar)} kayit satiri okundu")
except Exception as e:
    kayit("T1", False, f"dosya acilamadi: {e}")
    sys.exit(1)

idler = [s.get("siparis_id", "") for s in satirlar]
kayit("T2", len(satirlar) == 240 and len(set(idler)) == 240,
      f"{len(satirlar)} satir, {len(set(idler))} benzersiz siparis_id")

sutunlar = list(satirlar[0].keys())
kayit("T3", sutunlar == SUTUNLAR, f"{len(sutunlar)} sutun, sira beklenenle ayni: {sutunlar == SUTUNLAR}")
if sutunlar != SUTUNLAR:
    sys.exit(1)

try:
    tarihler = [date.fromisoformat(s["siparis_tarihi"]) for s in satirlar]
    kayit("T4", min(tarihler) >= date(2026, 1, 1) and max(tarihler) <= date(2026, 9, 30),
          f"aralik {min(tarihler)} - {max(tarihler)}")
except ValueError as e:
    kayit("T4", False, f"tarih bicimi hatali: {e}")

try:
    ok = (all(int(s["miktar"]) >= 10 for s in satirlar)
          and all(float(s["birim_fiyat_tl"]) > 0 for s in satirlar)
          and all(2 <= int(s["teslim_suresi_gun"]) <= 18 for s in satirlar))
    kayit("T5", ok, "miktar >= 10, birim_fiyat_tl > 0, teslim_suresi_gun 2-18")
except ValueError as e:
    kayit("T5", False, f"tip hatasi: {e}")

fark = max(abs(float(s["toplam_tutar_tl"]) - int(s["miktar"]) * float(s["birim_fiyat_tl"])) for s in satirlar)
bos = sum(1 for s in satirlar for v in s.values() if v == "")
kayit("T6", fark <= 0.01 and bos == 0, f"en buyuk fark {fark:.4f} TL, bos deger {bos}")

d = {c: {s[c] for s in satirlar} for c in ["tedarikci", "urun_kategorisi", "depo_bolgesi", "teslimat_durumu"]}
ok7 = (len(d["tedarikci"]) == 6 and len(d["urun_kategorisi"]) == 5
       and len(d["depo_bolgesi"]) == 5
       and d["teslimat_durumu"] == {"Zamanında", "Gecikmiş", "Kısmi Teslim"})
kayit("T7", ok7, f"tedarikci {len(d['tedarikci'])}, kategori {len(d['urun_kategorisi'])}, "
                 f"bolge {len(d['depo_bolgesi'])}, durum {len(d['teslimat_durumu'])}")

print(f"\nOzet: {sum(sonuclar)}/{len(sonuclar)} GECTI")
sys.exit(0 if all(sonuclar) else 1)
