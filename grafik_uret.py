"""FE görselleştirme betiği: data/tedarik_siparisleri.csv -> visuals/*.png
Kullanım (kök dizinden): python src/grafik_uret.py
Grafikler yalnızca BE'nin CSV'sinden hesaplanır; sabit veri yoktur."""
import csv
from collections import defaultdict
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

KOK = Path(__file__).resolve().parent.parent
CSV = KOK / "data" / "tedarik_siparisleri.csv"
CIKTI = KOK / "visuals"
MAVI, GRI = "#2A6F97", "#6B7280"
AYLAR = {"01": "Oca", "02": "Şub", "03": "Mar", "04": "Nis", "05": "May",
         "06": "Haz", "07": "Tem", "08": "Ağu", "09": "Eyl", "10": "Eki", "11": "Kas", "12": "Ara"}

aylik, kategori = defaultdict(float), defaultdict(float)
with open(CSV, encoding="utf-8") as f:
    for r in csv.DictReader(f):
        t = float(r["toplam_tutar_tl"])
        aylik[r["siparis_tarihi"][5:7]] += t
        kategori[r["urun_kategorisi"]] += t

def stil(ax):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.grid(axis="y", color="#E5E7EB", linewidth=0.8)
    ax.set_axisbelow(True)

# 1) Zaman serisi: aylık toplam sipariş tutarı
ay = sorted(aylik)
y = [aylik[a] / 1e6 for a in ay]
fig, ax = plt.subplots(figsize=(8, 4.5), dpi=120)
ax.plot([AYLAR[a] for a in ay], y, color=MAVI, linewidth=2, marker="o", markersize=7)
zi = y.index(max(y))
ax.annotate(f"{y[zi]:.2f} M TL", (zi, y[zi]), textcoords="offset points", xytext=(0, 10), ha="center", color=GRI)
ax.set_title("Aylık toplam sipariş tutarı (Ocak–Eylül 2026)", loc="left", fontweight="bold")
ax.set_xlabel("Ay (2026)")
ax.set_ylabel("Toplam tutar (milyon TL)")
ax.set_ylim(0, max(y) * 1.2)
stil(ax)
fig.tight_layout()
fig.savefig(CIKTI / "zaman_serisi.png")

# 2) Kırılım: ürün kategorisine göre toplam tutar
k = sorted(kategori.items(), key=lambda x: x[1], reverse=True)
toplam = sum(v for _, v in k)
fig, ax = plt.subplots(figsize=(8, 4.5), dpi=120)
bars = ax.bar([n for n, _ in k], [v / 1e6 for _, v in k], color=MAVI, width=0.6)
for b, (_, v) in zip(bars, k):
    ax.annotate(f"{v/1e6:.2f} M TL\n(%{v/toplam*100:.1f})", (b.get_x() + b.get_width() / 2, b.get_height()),
                textcoords="offset points", xytext=(0, 4), ha="center", fontsize=9, color=GRI)
ax.set_title("Ürün kategorisine göre toplam sipariş tutarı", loc="left", fontweight="bold")
ax.set_xlabel("Ürün kategorisi")
ax.set_ylabel("Toplam tutar (milyon TL)")
ax.set_ylim(0, max(v for _, v in k) / 1e6 * 1.25)
stil(ax)
fig.tight_layout()
fig.savefig(CIKTI / "kirilim.png")
print("Yazıldı:", CIKTI / "zaman_serisi.png", CIKTI / "kirilim.png")
