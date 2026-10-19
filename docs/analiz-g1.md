\# Analiz — Görev 1 (Tedarik)



\*\*Hazırlayan:\*\* Serra Erdem (DQ) · \*\*Kaynak:\*\* `data/tedarik\_siparisleri.csv` (240 sipariş, 2026-01-01 – 2026-09-30) · \*\*Betik:\*\* `src/analiz\_g1.py`



\## Metrikler



\### M1 — Toplam sipariş tutarı (toplam)

\*\*11.493.200,49 TL\*\* (240 sipariş).

Dokuz ayda yaklaşık 11,5 milyon TL'lik tedarik yapılmış; sipariş başına ortalama yaklaşık 47,9 bin TL düşüyor.



\### M2 — Ortalama teslim süresi (ortalama)

\*\*8,04 gün\*\* (geçerli aralık 2–18 gün).

Ortalama süre aralığın orta bölgesinde; gecikmiş siparişlere 3–8 gün eklendiği için uç değerler bu grupta yoğunlaşır.



\### M3 — Ürün kategorisine göre toplam tutar (kırılım 1)

| Kategori | Toplam tutar (TL) | Pay |

|---|---|---|

| Elektronik | 3.783.987,56 | %32,9 |

| Hammadde | 3.374.012,89 | %29,4 |

| Kimyasal | 1.828.649,80 | %15,9 |

| Yedek Parça | 1.320.747,74 | %11,5 |

| Ambalaj | 1.185.802,50 | %10,3 |



Elektronik ve Hammadde birlikte harcamanın yaklaşık %62'sini oluşturuyor. Ambalaj ve Yedek Parça toplamın beşte birinden azını kapsıyor.



\### M4 — Tedarikçiye göre gecikme oranı (kırılım 2)

| Tedarikçi | Gecikme oranı | Gecikmiş / Toplam |

|---|---|---|

| Akdeniz Ticaret | %21,1 | 8 / 38 |

| Marmara Endüstri | %14,6 | 6 / 41 |

| Ege Lojistik Ltd. | %13,9 | 5 / 36 |

| Anadolu Tedarik A.Ş. | %11,1 | 5 / 45 |

| Karadeniz Hammadde | %10,0 | 4 / 40 |

| Trakya Paketleme | %5,0 | 2 / 40 |



Genel gecikme oranı %12,5 (30/240). Akdeniz Ticaret bu ortalamanın yaklaşık 1,7 katı, Trakya Paketleme ise en düşük orana sahip.



\### M5 — Toplam tutara göre ilk 3 tedarikçi (top-3)

| Sıra | Tedarikçi | Toplam tutar (TL) |

|---|---|---|

| 1 | Anadolu Tedarik A.Ş. | 2.327.144,83 |

| 2 | Marmara Endüstri | 2.244.374,22 |

| 3 | Trakya Paketleme | 2.088.743,97 |



Bu üç tedarikçi toplam tutarın yaklaşık %58'ini alıyor. Listedeki Trakya Paketleme aynı zamanda en az gecikme yapan tedarikçi.



\### M6 — Aylık sipariş sayısı (ek metrik)

| Ay | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 |

|---|---|---|---|---|---|---|---|---|---|

| Sipariş | 19 | 18 | 27 | 38 | 33 | 36 | 24 | 16 | 29 |



Sipariş hacmi Nisan–Haziran döneminde zirve yapıyor, Ağustos'ta dip noktaya iniyor, Eylül'de toparlanıyor.



\## Somut gözlemler



1\. \*\*Harcama iki kategoride toplanıyor.\*\* Elektronik (%32,9) ve Hammadde (%29,4) toplam tutarın yaklaşık %62'sini oluşturuyor; bütçe ve fiyat takibinin ağırlığı bu iki kategoride olmalı.

2\. \*\*Gecikme riski tedarikçiye göre keskin biçimde değişiyor.\*\* Akdeniz Ticaret'in gecikme oranı (%21,1), Trakya Paketleme'nin (%5,0) yaklaşık 4 katı. Genel ortalama %12,5.

3\. \*\*Siparişler mevsimsel.\*\* Nisan–Haziran'da 107 sipariş (toplamın yaklaşık %45'i) verilmiş, Ağustos'ta yalnızca 16.Eylül, Ağustos'taki düşüşten sonra toparlanma ayıdır (29 sipariş).


\## Eylem önerisi



Akdeniz Ticaret'e verilen siparişlerin bir kısmının gecikme oranı düşük olan tedarikçilere (örn. Trakya Paketleme, Karadeniz Hammadde) kaydırılması ve Akdeniz Ticaret için teslim süresi taahhüdü (SLA) istenmesi önerilir. Veri sözlüğüne göre bu tedarikçi en düşük fiyat düzeyine sahip olduğundan, kararda maliyet ile gecikme riski birlikte tartılmalıdır.



\## Sınırlılıklar



Veri sentetiktir (seed=42). Tedarikçi başına 36–45 sipariş bulunduğundan oranlar küçük örnekleme dayanır; birkaç gecikmenin sayısı bile oranı belirgin biçimde değiştirir.

