import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Gerçek CSV dosyasını ve sütun adlarını kullanıyoruz
df = pd.read_csv('data/tedarik_siparisleri.csv')

# Tarih sütununu tarihe çevirip ay bilgisini çekelim
df['siparis_tarihi'] = pd.to_datetime(df['siparis_tarihi'])
df['ay'] = df['siparis_tarihi'].dt.to_period('M').astype(str)

# 1. Grafik: Zaman Serisi
aylik_siparis = df.groupby('ay').size()

plt.figure(figsize=(8, 5))
plt.plot(aylik_siparis.index, aylik_siparis.values, marker='o', color='b')
plt.title('Aylara Göre Sipariş Sayısı')
plt.xlabel('Aylar')
plt.ylabel('Sipariş Sayısı (Adet)')
plt.grid(True)
plt.savefig('visuals/zaman_serisi.png')
plt.close()

# 2. Grafik: Kırılım (Gerçek sütunlar: urun_kategorisi ve toplam_tutar_tl)
kategori_tutar = df.groupby('urun_kategorisi')['toplam_tutar_tl'].sum()

plt.figure(figsize=(8, 5))
kategori_tutar.plot(kind='bar', color='orange')
plt.title('Ürün Kategorisine Göre Toplam Tutar')
plt.xlabel('Kategoriler')
plt.ylabel('Toplam Tutar (TL)')
plt.grid(axis='y')

# Arkadaşın eleştirisindeki TL eksenine binlik ayraç (FuncFormatter) formatı
plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f"{x:,.0f} TL"))

plt.savefig('visuals/kirilim.png')
plt.close()