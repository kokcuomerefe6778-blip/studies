import random

rastgele_sayi = random.randint(1, 10)
can = 5 

print("1-10 arasi bir sayi tuttum.")
print("Toplam", can, "hakkin var.")
print("---------------------------------")
while can > 0:
    tahmin = int(input("Tahminin: "))

    if tahmin == rastgele_sayi:
        print("Tebrikler sayiyi buldun.")
        break  
        
    elif tahmin < rastgele_sayi:
        print("Yanlis! Biraz daha buyuk bir sayi soyle.")
    else:
        print("Yanlis! Biraz daha kucuk bir sayi soyle.")

    can = can - 1

    if can > 0:
        print("Kalan canin:", can)
        print("---------------------------------")
    else:
        print("Canin bitti ve kaybettin!")
        print("Tuttugum sayi suydu:", rastgele_sayi)