# G1 analiz - Serra Erdem (DQ)
import csv
from collections import defaultdict

with open("data/tedarik_siparisleri.csv", encoding="utf-8-sig", newline="") as f:
    satirlar = list(csv.DictReader(f))

cikti = []
def yaz(metin=""):
    cikti.append(metin)

n = len(satirlar)
toplam_tutar = sum(float(s["toplam_tutar_tl"]) for s in satirlar)
ort_sure = sum(int(s["teslim_suresi_gun"]) for s in satirlar) / n

yaz(f"Satir sayisi: {n}")
yaz(f"M1 Toplam tutar (TL): {toplam_tutar:,.2f}")
yaz(f"M2 Ortalama teslim suresi (gun): {ort_sure:.2f}")

# M3: kategori bazinda toplam tutar
kat = defaultdict(float)
for s in satirlar:
    kat[s["urun_kategorisi"]] += float(s["toplam_tutar_tl"])
yaz("\nM3 Kategori bazinda toplam tutar (TL):")
for k, v in sorted(kat.items(), key=lambda x: -x[1]):
    yaz(f"  {k}: {v:,.2f} (pay %{100 * v / toplam_tutar:.1f})")

# M4: tedarikci bazinda gecikme orani
sayi = defaultdict(int)
gec = defaultdict(int)
for s in satirlar:
    t = s["tedarikci"]
    sayi[t] += 1
    if s["teslimat_durumu"] == "Gecikmiş":
        gec[t] += 1
yaz("\nM4 Tedarikci bazinda gecikme orani:")
for t in sorted(sayi, key=lambda x: -gec[x] / sayi[x]):
    yaz(f"  {t}: %{100 * gec[t] / sayi[t]:.1f} ({gec[t]}/{sayi[t]})")

# M5: tedarikci bazinda toplam tutar, ilk 3
ted = defaultdict(float)
for s in satirlar:
    ted[s["tedarikci"]] += float(s["toplam_tutar_tl"])
yaz("\nM5 Toplam tutara gore ilk 3 tedarikci (TL):")
for t, v in sorted(ted.items(), key=lambda x: -x[1])[:3]:
    yaz(f"  {t}: {v:,.2f}")

# M6 (ek): aylik siparis sayisi
ay = defaultdict(int)
for s in satirlar:
    ay[s["siparis_tarihi"][:7]] += 1
yaz("\nM6 Aylik siparis sayisi:")
for a in sorted(ay):
    yaz(f"  {a}: {ay[a]}")

# Teslimat durumu dagilimi
durum = defaultdict(int)
for s in satirlar:
    durum[s["teslimat_durumu"]] += 1
yaz("\nTeslimat durumu dagilimi:")
for d, c in durum.items():
    yaz(f"  {d}: {c}")

with open("analiz_ciktisi.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(cikti))
print("Tamam: analiz_ciktisi.txt olustu")