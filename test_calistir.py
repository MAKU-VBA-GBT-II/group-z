import csv, re
from datetime import date

YOL = "data/tedarik_siparisleri.csv"
SUTUNLAR = ["siparis_id","siparis_tarihi","tedarikci","urun_kategorisi",
            "depo_bolgesi","miktar","birim_fiyat_tl","toplam_tutar_tl",
            "teslim_suresi_gun","teslimat_durumu"]

def sonuc(no, ad, hatalar, bilgi=""):
    d = "GEÇTİ" if not hatalar else "KALDI"
    print(f"\n{no} {ad}: {d}")
    if bilgi: print("  Bilgi:", bilgi)
    for h in hatalar[:5]: print("  -", h)
    if len(hatalar) > 5: print(f"  ... toplam {len(hatalar)} sorun")

h = []
satirlar = []
basliklar = []
try:
    with open(YOL, encoding="utf-8", newline="") as f:
        okuyucu = csv.DictReader(f, delimiter=",")
        basliklar = okuyucu.fieldnames
        satirlar = list(okuyucu)
except Exception as e:
    h.append(str(e))
sonuc("T1", "Dosya var mi", h, f"{len(satirlar)} satir okundu")

h = []
ids = [r["siparis_id"] for r in satirlar]
if len(satirlar) != 240: h.append(f"Satir sayisi {len(satirlar)}, beklenen 240")
if len(set(ids)) != len(ids): h.append("siparis_id tekrar ediyor")
if sorted(ids) != [f"SIP-{i:04d}" for i in range(1, 241)]: h.append("siparis_id SIP-0001...SIP-0240 degil")
sonuc("T2", "Satir sayisi", h)

h = []
if basliklar != SUTUNLAR: h.append(f"Sutunlar farkli: {basliklar}")
sonuc("T3", "Sutunlar", h)

h = []
for r in satirlar:
    t = r["siparis_tarihi"]
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", t):
        h.append(f"{r['siparis_id']}: bicim hatali '{t}'"); continue
    try:
        y, a, g = map(int, t.split("-"))
        if not (date(2026,1,1) <= date(y,a,g) <= date(2026,9,30)):
            h.append(f"{r['siparis_id']}: aralik disi {t}")
    except ValueError:
        h.append(f"{r['siparis_id']}: gecersiz tarih {t}")
sonuc("T4", "Tarih", h)

h = []
for r in satirlar:
    i = r["siparis_id"]
    if not re.fullmatch(r"\d+", r["miktar"]) or int(r["miktar"]) < 10:
        h.append(f"{i}: miktar {r['miktar']} (tam sayi ve >=10 olmali)")
    try:
        fiyat = float(r["birim_fiyat_tl"])
        if fiyat <= 0: h.append(f"{i}: birim_fiyat_tl {fiyat} (>0 olmali)")
        if round(fiyat, 2) != fiyat: h.append(f"{i}: fiyat 2 ondaliktan fazla")
    except Exception:
        h.append(f"{i}: birim_fiyat_tl okunamadi")
    if not re.fullmatch(r"\d+", r["teslim_suresi_gun"]) or not (2 <= int(r["teslim_suresi_gun"]) <= 18):
        h.append(f"{i}: teslim_suresi_gun {r['teslim_suresi_gun']} (2-18 olmali)")
sonuc("T5", "Tipler / araliklar", h)

h = []
for r in satirlar:
    i = r["siparis_id"]
    for k, v in r.items():
        if v is None or v.strip() == "": h.append(f"{i}: '{k}' bos")
    try:
        beklenen = float(r["miktar"]) * float(r["birim_fiyat_tl"])
        if abs(beklenen - float(r["toplam_tutar_tl"])) > 0.01:
            h.append(f"{i}: toplam {r['toplam_tutar_tl']}, beklenen {beklenen:.2f}")
    except Exception:
        pass
sonuc("T6", "Tutarlilik", h)

h = []
d = {k: sorted(set(r[k] for r in satirlar))
     for k in ["tedarikci","urun_kategorisi","depo_bolgesi","teslimat_durumu"]}
if len(d["tedarikci"]) != 6: h.append("tedarikci 6 deger degil")
if d["urun_kategorisi"] != sorted(["Hammadde","Ambalaj","Elektronik","Kimyasal","Yedek Parça"]):
    h.append("urun_kategorisi beklenen 5 deger degil")
if d["depo_bolgesi"] != sorted(["Marmara","Ege","İç Anadolu","Akdeniz","Karadeniz"]):
    h.append("depo_bolgesi beklenen 5 deger degil")
if d["teslimat_durumu"] != sorted(["Zamanında","Gecikmiş","Kısmi Teslim"]):
    h.append("teslimat_durumu beklenen 3 deger degil")
sonuc("T7", "Kategori degerleri", h)
print("\nBulunan degerler:")
for k, v in d.items(): print(f"  {k}: {v}")