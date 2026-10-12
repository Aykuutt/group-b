import os
import random
import sys

# İpek ÖZARSLAN - Hafta 2 ısınma görevi
ADINIZ = "ipek"

if len(sys.argv) > 1:
    ADINIZ = sys.argv[1].strip()

# 1 ile 100 arasında (dahil) 10 adet rastgele sayı üret
rastgele_sayilar = [random.randint(1, 100) for _ in range(10)]

# Proje kök dizinini ve 'data' klasörünü belirle
proje_kok = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
data_klasoru = os.path.join(proje_kok, "data")
os.makedirs(data_klasoru, exist_ok=True)

# Çıktı dosya yolu: data/prova-ipek.csv
hedef_dosya = os.path.join(data_klasoru, f"prova-{ADINIZ}.csv")

# CSV formatında tek sütun halinde yaz (başlık: deger)
with open(hedef_dosya, "w", encoding="utf-8", newline="") as f:
    f.write("deger\n")
    for sayi in rastgele_sayilar:
        f.write(f"{sayi}\n")

print(f"CSV başarıyla oluşturuldu: {hedef_dosya}")
print(f"Üretilen 10 rastgele sayı: {rastgele_sayilar}")
