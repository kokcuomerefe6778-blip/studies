sayi = int(input("Sayi giriniz: "))

if sayi < 0:
    print("Pozitif sayi giriniz...")
elif sayi %2 == 0:
    print(f"{sayi} sayisi cifttir.")
else:
    print(f"{sayi} sayisi tektir.")    