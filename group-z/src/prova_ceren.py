import random
import csv
import os

# data klasörü yoksa oluştur
os.makedirs("data", exist_ok=True)

with open("data/prova-ceren.csv", "w", newline="") as f:
    yazar = csv.writer(f)
    yazar.writerow(["deger"])          # başlık satırı
    for _ in range(10):
        yazar.writerow([random.randint(1, 100)])   # 1-100 arası sayı