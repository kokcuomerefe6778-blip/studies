Sayi = int(input("Bir sayı giriniz: "))
isAsal = True

if Sayi < 0:
    print("Negatif sayılar asal sayı olamaz.")
elif Sayi == 0 or Sayi == 1:
    print(f"{Sayi} asal sayı değildir. En küçük asal sayı 2'dir.")
else:
    for i in range(2, int(Sayi**0.5) + 1):
        if Sayi % i == 0:
            isAsal = False
            break   
    if isAsal:
        print(f"{Sayi} bir asal sayıdır.")   
    else:
        print(f"{Sayi} asal sayı değildir.")