print("---HESAP MAKINESI---")

while True:
    print("\nIslmeler: [+] Toplama, [-] Cikarma, [*]Carpma, [/] Bolme")
    secim = input("Islem seciniz (q = Cikis): ")

    if secim == 'q':
        print("Hesap makinsinden cikiliyor...")
        break

    if secim != '+' and secim != '-' and secim != '*' and secim != '/':
        print("Gecersiz islem! Lutfen tekrar deneyiniz.")
        continue

    sayi1 = float(input("Birinci sayi: "))
    sayi2 = float(input("Ikinci sayi: "))

    if secim == '+':
        sonuc = sayi1 + sayi2 
        print("Sonuc: ", sonuc)
    elif secim == '-':
        sonuc = sayi1 - sayi2 
        print("Sonuc: ", sonuc)    
    elif secim == '*':
        sonuc = sayi1 * sayi2 
        print("Sonuc: ", sonuc)
    elif secim == '/':
        if sayi2 == 0:
            print("Hata: Ikinci sayi sifir olamaz!")
        else:
            sonuc = sayi1 / sayi2
            print("Sonuc: ", sonuc)
        