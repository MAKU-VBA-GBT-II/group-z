#!/usr/bin/env python3
"""Tedarik sektörü için parametreli sentetik sipariş verisi üreticisi.

Şema: docs/veri-sozlugu.md (DQ, commit 57b7543) ile birebir uyumludur.
Yalnızca Python standart kütüphanesini kullanır.

Ayarlanabilir parametreler:
  --seed      rastgelelik tohumu            (varsayılan: 42)
  --satir     üretilecek sipariş sayısı     (varsayılan: 240)
  --tedarikci kullanılacak tedarikçi sayısı (1-6, varsayılan: 6)
  --cikti     çıktı CSV yolu                (varsayılan: data/tedarik_siparisleri.csv)

Varsayılan değerlerle (seed=42, 240 satır) her çalıştırmada aynı dosya üretilir.
"""
import argparse
import csv
import random
from datetime import date, timedelta
from pathlib import Path

BASLANGIC = date(2026, 1, 1)
BITIS = date(2026, 9, 30)

ALANLAR = [
    "siparis_id", "siparis_tarihi", "tedarikci", "urun_kategorisi",
    "depo_bolgesi", "miktar", "birim_fiyat_tl", "toplam_tutar_tl",
    "teslim_suresi_gun", "teslimat_durumu",
]

# tedarikçi: (gecikme olasılığı, fiyat çarpanı)
TEDARIKCILER = {
    "Anadolu Tedarik A.Ş.": (0.10, 1.00),
    "Ege Lojistik Ltd.": (0.22, 0.92),
    "Marmara Endüstri": (0.12, 1.08),
    "Akdeniz Ticaret": (0.18, 0.95),
    "Karadeniz Hammadde": (0.25, 0.88),
    "Trakya Paketleme": (0.08, 1.05),
}

# kategori: (miktar min, miktar max, birim fiyat min, birim fiyat max)
KATEGORILER = {
    "Hammadde": (200, 5000, 8.0, 60.0),
    "Ambalaj": (300, 5000, 1.5, 15.0),
    "Yedek Parça": (10, 400, 80.0, 1500.0),
    "Elektronik": (10, 600, 50.0, 900.0),
    "Kimyasal": (50, 2000, 15.0, 250.0),
}

DEPOLAR = ["Marmara", "Ege", "İç Anadolu", "Akdeniz", "Karadeniz"]

# Ay ağırlıkları: Nisan–Haziran yoğun, Ağustos en sakin
AY_AGIRLIK = {1: 6, 2: 6, 3: 8, 4: 13, 5: 14, 6: 13, 7: 8, 8: 4, 9: 7}


def rastgele_tarih(rng):
    gunler = [BASLANGIC + timedelta(days=i)
              for i in range((BITIS - BASLANGIC).days + 1)]
    agirlik = [AY_AGIRLIK[g.month] * (0.1 if g.weekday() >= 5 else 1.0)
               for g in gunler]  # hafta sonu nadir
    return rng.choices(gunler, weights=agirlik, k=1)[0]


def uret(seed=42, satir=240, tedarikci_sayisi=6):
    if not 1 <= tedarikci_sayisi <= len(TEDARIKCILER):
        raise ValueError("tedarikci sayısı 1 ile 6 arasında olmalı")
    if satir < 1:
        raise ValueError("satır sayısı en az 1 olmalı")

    rng = random.Random(seed)
    tedarikciler = list(TEDARIKCILER)[:tedarikci_sayisi]
    tarihler = sorted(rastgele_tarih(rng) for _ in range(satir))

    kayitlar = []
    for i, tarih in enumerate(tarihler, start=1):
        ted = rng.choice(tedarikciler)
        gecikme_olas, fiyat_carpan = TEDARIKCILER[ted]
        kat = rng.choice(list(KATEGORILER))
        q_min, q_max, f_min, f_max = KATEGORILER[kat]

        miktar = rng.randint(q_min, q_max)
        fiyat = round(rng.uniform(f_min, f_max) * fiyat_carpan, 2)
        toplam = round(miktar * fiyat, 2)

        sure = rng.randint(2, 10)
        r = rng.random()
        if r < gecikme_olas:
            durum = "Gecikmiş"
            sure += rng.randint(3, 8)
        elif r < gecikme_olas + 0.08:
            durum = "Kısmi Teslim"
        else:
            durum = "Zamanında"
        sure = min(sure, 18)

        kayitlar.append({
            "siparis_id": f"SIP-{i:04d}",
            "siparis_tarihi": tarih.isoformat(),
            "tedarikci": ted,
            "urun_kategorisi": kat,
            "depo_bolgesi": rng.choice(DEPOLAR),
            "miktar": miktar,
            "birim_fiyat_tl": f"{fiyat:.2f}",
            "toplam_tutar_tl": f"{toplam:.2f}",
            "teslim_suresi_gun": sure,
            "teslimat_durumu": durum,
        })
    return kayitlar


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--seed", type=int, default=42, help="rastgelelik tohumu")
    p.add_argument("--satir", type=int, default=240, help="sipariş sayısı")
    p.add_argument("--tedarikci", type=int, default=6, help="tedarikçi sayısı (1-6)")
    p.add_argument("--cikti", default="data/tedarik_siparisleri.csv", help="çıktı yolu")
    a = p.parse_args()

    kayitlar = uret(a.seed, a.satir, a.tedarikci)
    yol = Path(a.cikti)
    yol.parent.mkdir(parents=True, exist_ok=True)
    with open(yol, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=ALANLAR)
        w.writeheader()
        w.writerows(kayitlar)

    print(f"{yol}: {len(kayitlar)} satır, {len(ALANLAR)} alan "
          f"(seed={a.seed}, tedarikçi={a.tedarikci})")
    print("Sütunlar:", ", ".join(ALANLAR))


if __name__ == "__main__":
    main()
