--- 
name: dq-analiz 
description: Tedarik siparis verisinden 5 metrik hesaplar ve docs/analiz-g1.md dosyasini uretir. 
--- 
 
# dq-analiz 
 
Girdi: data/tedarik_siparisleri.csv, docs/veri-sozlugu-g1.md, BE nin Veri hazir yorumu. 
 
Adimlar: src/analiz_g1.py ile toplam tutar, ortalama teslim suresi, kategori kirilimi, tedarikci gecikme orani, ilk 3 tedarikci ve aylik siparis sayisini hesapla. Her metrige yorum, 3 gozlem ve 1 eylem onerisi yaz. 
 
Cikti: docs/analiz-g1.md, src/analiz_g1.py 
