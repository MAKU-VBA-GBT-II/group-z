import random
import csv
from pathlib import Path

# 1 ile 100 arasında 10 rastgele sayı üret
degerler = [random.randint(1, 100) for _ in range(10)]

# Ana proje klasörünü bul ve data klasörünü belirle
proje_klasoru = Path(__file__).resolve().parent.parent
data_klasoru = proje_klasoru / "data"

# data klasörü yoksa oluştur
data_klasoru.mkdir(exist_ok=True)

# Sayıları CSV dosyasına yaz
dosya_yolu = data_klasoru / "prova-irem.csv"

with open(dosya_yolu, "w", newline="", encoding="utf-8") as dosya:
    yazici = csv.writer(dosya)
    yazici.writerow(["deger"])
    for sayi in degerler:
        yazici.writerow([sayi])

print("CSV dosyası başarıyla oluşturuldu!")
print(f"Dosya konumu: {dosya_yolu}")