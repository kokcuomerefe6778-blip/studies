Sayi = int(input("Bir sayı giriniz: "))
isAsal = True
if (Sayi < 0):
    print("Negatif sayılar asal sayı olamaz.")
elif (Sayi > 0 and Sayi < 2):
    print("2 en küçük asal sayıdır.")
else:
    for i in range(2, int(Sayi**0.5)+1):
        if (Sayi % i == 0):
            print("Bu sayı asal sayı değildir.")
            isAsal = False
            break
    if (isAsal):
        print(f"{Sayi}Bu sayı asal sayıdır.")   
    else:
        print(f"{Sayi}Bu sayı asal sayı değildir.")     
    