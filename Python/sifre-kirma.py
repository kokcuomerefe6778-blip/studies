import time

hedef_sifre = "654"
deneme = 0

print("Sifre kirma programi baslatildi.")
baslangic_zamani = time.time()

for i in range(1000):
    deneme += 1
    uretilen_sifre = str(i).zfill(3)

    if uretilen_sifre == hedef_sifre:
        print(f"Sifre bulundu: {hedef_sifre}")
        print(f"Toplam deneme: {deneme}")
        break

bitis_zamani = time.time()
gecen_sure = bitis_zamani - baslangic_zamani

print(f"Sifre kirma islemi {gecen_sure:.4f} saniye sürdü.")
