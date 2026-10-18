---
name: pm-rapor
description: Grup Z'nin haftalık sprint raporunu (reports/report-wNN.md) GitHub Issue ve pano verisinden üretir.
---

# pm-rapor

## Ne yapar
Grubun Görev 1 Issue'larını (G1-veri, G1-analiz, G1-gorsel, G1-test) ve devir yorumlarını okuyup haftalık sprint raporunu üretir: planlanan / yapılan / tıkanan / kim ne yaptı.

## Adım adım talimat
1. Grup deposundaki 4 Issue'yu listele (başlık, sorumlu, son tarih, durum).
2. Her Issue'daki yorumlarda "hazır — commit <hash>" biçimindeki devir yorumunu ara.
3. Planlanan: dört Issue'nun başlığı, sorumlusu ve son tarihi.
4. Yapılan: devir yorumu olan Issue'lar (commit hash'iyle birlikte).
5. Tıkanan: son tarihi geçmiş veya devir yorumu olmayan Issue'lar, nedeniyle birlikte.
6. Kim ne yaptı: her üyenin teslim ettiği dosya ve commit.
7. Çıktıyı reports/report-wNN.md olarak yaz (NN = hafta numarası, örn. w03).
8. Dosyayı repoya commit'le.

## Kullandığı dosyalar
- Girdi: GitHub Issue'ları (#7, #8, #9, #10), Görev 1 Panosu
- Girdi: AGENTS.md (skill envanteri)
- Çıktı: reports/report-w03.md

## Nasıl çalıştırılır
Bir yapay zekâ ajanına (Claude, Codex vb.) şu komut verilir:
"skills/pm-rapor/SKILL.md talimatını izleyerek bu haftanın raporunu reports/report-w03.md olarak üret."
Ajan Issue'ları okur, raporu yazar; çıktı repoya commit'lenir.
