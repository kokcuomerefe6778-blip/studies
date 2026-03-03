sayi_giriniz = int(input("Bir sayı giriniz: "))
asal_sayi = []
if sayi_giriniz < 0:
    print("Negatif sayılar asal sayı olamaz.")
elif sayi_giriniz <2:
    print("2 en küçük asal sayıdır.")
else:
    asal_sayi.append(2)
    for i in range(3, sayi_giriniz+1, 2):
        for j in range(3, int(i**0.5)+1):
            if (i % j == 0):
                break
        else:
            asal_sayi.append(i)
    print(f"Bulunan asal sayılar: {asal_sayi}")