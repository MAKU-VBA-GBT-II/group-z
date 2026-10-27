# Hafta 4 Sprint Raporu — Grup Z (Tedarik)

**Hazırlayan:** İrem Deneri (PM) · **Dönem:** Hafta 4 (Görev 1 Kapanış, Test & Sürüm) · **Tarih:** 27 Ekim 2026

---

## 1. Planlanan İşler

- Hafta 3 denetiminde tespit edilen blokajların (BE devir teslimi, FE skill/taslak eksikliği, DQ analiz uyuşmazlığı) kapatılması.
- DQ tarafından senaryoların gerçek veri üzerinde koşturulup günlüğüne işlenmesi: `tests/test-cases.md` `tests/test-log.md`
- DQ tarafından en az 2 adet hata/iyileştirme Issue'su açılması ve ilgili rollere atanması.
- BE ve FE rollerinin kendilerine atanan Issue'ları düzeltme commit'leriyle kapatması.
- DQ'nun nihai veri ve şema uyumunu onaylaması.
- Görev 1'in tüm gereksinimleri tamamlanarak resmi sürümün yayımlanması: `gorev1-final`

---

## 2. Kim Ne Yaptı? (Teslimat ve Kanıt Tablosu)

| Rol | Kişi | Görev Kodu | Issue'lar | Yapılan İş & Teslim Edilen Dosyalar | Durum |
|-----|------|------------|-----------|-------------------------------------|-------|
| PM | İrem Deneri | PM-Kapanış | #16, #17, #18 | Grup E ile yürütülen çapraz inceleme Issue'ları açıldı ve kapatıldı; `report-w03.md`, `report-w04.md` ve `AGENTS.md` güncellendi. | Devam ediyor |
| BE | Ceren Gözel | G1-Düzeltme | #22 | `data/tedarik_siparisleri.csv` veri dosyası düzeltmesi ve devir yorumu. | Devam ediyor |
| DQ | Serra Erdem | G1-Test & Onay | #14, #22, #23 | `tests/test-cases.md` (T1–T7) hazırlandı ve koşturuldu; #22 (Hata) ve #23 (Geliştirme) Issue'ları açıldı. `tests/test-log.md` | Tamamlandı |
| FE | Baki Korkmaz | G1-Görsel | #13 | `skills/fe-gorsel/SKILL.md` ve grafik revizyonları. | Devam ediyor |

---

## 3. Test ve Kalite Süreci (DQ Rapor Özeti)

- `tests/test-cases.md` altındaki 7 senaryo (T1–T7), `python test_calistir.py` ile `data/tedarik_siparisleri.csv` üzerinde 27.10.2026 tarihinde koşturulmuş ve `tests/test-log.md` dosyasına işlenmiştir.
- İlk koşuda T1 (dosya açılabiliyor mu) geçmiş, T2–T7 kalmıştır. Neden: repodaki veri dosyası (4 satır, 3 sütun) test senaryolarının yazıldığı veri setiyle (240 satır, 10 sütun) aynı değildir.
- Bu bulgu için DQ tarafından Hata Issue'su (#22) açılmıştır. Ayrıca `teslim_suresi_gun` için üst sınır eklenmesini öneren Geliştirme Issue'su (#23) açılmıştır.
- Veri dosyası düzeltildikten sonra T2–T7'nin yeniden koşturulması ve `tests/test-log.md`'nin güncellenmesi gerekmektedir.

---

## 4. Açık Konular

- #23 (Geliştirme): `teslim_suresi_gun` için üst sınır eklenmeli. Durum: açık.
- Veri dosyası düzeltmesi sonrası testler tekrar koşulacak ve test logu güncellenecek.
- DQ'nun nihai veri üzerinde `docs/veri-sozlugu-g1.md` şema onayı ve G1-analiz kapanış yorumu, testler geçtikten sonra yapılacak.

---

## 5. Kapanış ve Sürüm

Görev 1 kapsamındaki gereksinimlerin büyük bölümü tamamlanmıştır. Kalan açık konular (bölüm 4) kapandıktan sonra `gorev1-final` etiketiyle GitHub Releases üzerinden sürüm yayımlanacaktır.
