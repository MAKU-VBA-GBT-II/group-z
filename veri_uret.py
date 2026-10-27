#!/usr/bin/env python3
"""Tedarik sektörü sentetik sipariş verisi üreticisi (Görev 1 — BE).

Sabit tohum (seed) kullanır: aynı parametrelerle her çalıştırmada
birebir aynı CSV üretilir. Yalnızca Python standart kütüphanesi gerekir.

Kullanım (repo kök dizininden):
    python src/veri_uret.py
    python src/veri_uret.py --seed 42 --satir 240
"""
import argparse
import csv
import random
from datetime import date, timedelta
from pathlib import Path

VARSAYILAN_TOHUM = 42
VARSAYILAN_SATIR = 240
BASLANGIC = date(2026, 1, 1)
BITIS = date(2026, 9, 30)

# kategori: (min_miktar, max_miktar, min_birim_fiyat, max_birim_fiyat, secilme_agirligi)
KATEGORILER = {
    "Hammadde": (200, 2000, 15, 80, 0.30),
    "Ambalaj": (500, 5000, 2, 12, 0.25),
    "Elektronik": (20, 300, 150, 900, 0.15),
    "Kimyasal": (50, 800, 40, 220, 0.15),
    "Yedek Parça": (10, 200, 60, 500, 0.15),
}

# tedarikçi: (gecikme_olasiligi, kismi_teslim_olasiligi, ortalama_teslim_gun, fiyat_carpani)
TEDARIKCILER = {
    "Anadolu Tedarik A.Ş.": (0.08, 0.04, 6, 1.00),
    "Ege Lojistik Ltd.": (0.15, 0.06, 8, 0.95),
    "Marmara Endüstri": (0.10, 0.05, 7, 1.05),
    "Akdeniz Ticaret": (0.25, 0.08, 10, 0.92),
    "Karadeniz Hammadde": (0.20, 0.07, 9, 0.97),
    "Trakya Paketleme": (0.12, 0.05, 5, 1.03),
}

BOLGELER = ["Marmara", "Ege", "İç Anadolu", "Akdeniz", "Karadeniz"]

# Ay bazlı talep çarpanı (zaman serisinde okunabilir bir desen olsun diye)
AY_AGIRLIK = {1: 0.8, 2: 0.9, 3: 1.0, 4: 1.0, 5: 1.1, 6: 1.1, 7: 0.9, 8: 0.8, 9: 1.3}

ALANLAR = [
    "siparis_id",
    "siparis_tarihi",
    "tedarikci",
    "urun_kategorisi",
    "depo_bolgesi",
    "miktar",
    "birim_fiyat_tl",
    "toplam_tutar_tl",
    "teslim_suresi_gun",
    "teslimat_durumu",
]


def gun_havuzu():
    """Tarih aralığındaki günleri ve seçilme ağırlıklarını döndürür."""
    gunler, agirliklar = [], []
    gun = BASLANGIC
    while gun <= BITIS:
        agirlik = AY_AGIRLIK[gun.month]
        if gun.weekday() >= 5:  # hafta sonu siparişi az
            agirlik *= 0.2
        gunler.append(gun)
        agirliklar.append(agirlik)
        gun += timedelta(days=1)
    return gunler, agirliklar


def uret(satir_sayisi, tohum):
    rng = random.Random(tohum)
    gunler, agirliklar = gun_havuzu()

    kat_adlari = list(KATEGORILER)
    kat_agirlik = [KATEGORILER[k][4] for k in kat_adlari]
    ted_adlari = list(TEDARIKCILER)

    kayitlar = []
    for _ in range(satir_sayisi):
        tarih = rng.choices(gunler, weights=agirliklar, k=1)[0]
        tedarikci = rng.choice(ted_adlari)
        kategori = rng.choices(kat_adlari, weights=kat_agirlik, k=1)[0]
        bolge = rng.choice(BOLGELER)

        min_m, max_m, min_f, max_f, _ = KATEGORILER[kategori]
        gecikme_p, kismi_p, ort_teslim, fiyat_carpani = TEDARIKCILER[tedarikci]

        miktar = rng.randint(min_m, max_m)
        birim_fiyat = round(rng.uniform(min_f, max_f) * fiyat_carpani, 2)
        toplam = round(miktar * birim_fiyat, 2)

        teslim = max(2, round(rng.gauss(ort_teslim, 1.5)))
        r = rng.random()
        if r < gecikme_p:
            durum = "Gecikmiş"
            teslim += rng.randint(3, 8)
        elif r < gecikme_p + kismi_p:
            durum = "Kısmi Teslim"
        else:
            durum = "Zamanında"

        kayitlar.append({
            "siparis_tarihi": tarih.isoformat(),
            "tedarikci": tedarikci,
            "urun_kategorisi": kategori,
            "depo_bolgesi": bolge,
            "miktar": miktar,
            "birim_fiyat_tl": f"{birim_fiyat:.2f}",
            "toplam_tutar_tl": f"{toplam:.2f}",
            "teslim_suresi_gun": teslim,
            "teslimat_durumu": durum,
        })

    kayitlar.sort(key=lambda k: k["siparis_tarihi"])
    for sira, kayit in enumerate(kayitlar, start=1):
        kayit["siparis_id"] = f"SIP-{sira:04d}"
    return kayitlar


def main():
    ap = argparse.ArgumentParser(description="Tedarik sentetik veri üretici")
    ap.add_argument("--seed", type=int, default=VARSAYILAN_TOHUM, help="rastgelelik tohumu")
    ap.add_argument("--satir", type=int, default=VARSAYILAN_SATIR, help="üretilecek satır sayısı")
    ap.add_argument("--cikti", default=None, help="çıktı CSV yolu (varsayılan: data/tedarik_siparisleri.csv)")
    args = ap.parse_args()

    kok = Path(__file__).resolve().parent.parent
    cikti = Path(args.cikti) if args.cikti else kok / "data" / "tedarik_siparisleri.csv"
    cikti.parent.mkdir(parents=True, exist_ok=True)

    kayitlar = uret(args.satir, args.seed)
    with open(cikti, "w", newline="", encoding="utf-8") as f:
        yazar = csv.DictWriter(f, fieldnames=ALANLAR, lineterminator="\n")
        yazar.writeheader()
        yazar.writerows(kayitlar)

    print(f"{len(kayitlar)} satır yazıldı -> {cikti} (seed={args.seed})")


if __name__ == "__main__":
    main()
