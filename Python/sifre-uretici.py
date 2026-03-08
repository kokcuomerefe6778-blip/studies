import random

harfler = "abcçdefgğhıijklmnoöprsştuüvyzABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"
rakalmar = "0123456789"
semboller = "!@#$%^&*()_+"

havuz = harfler + rakalmar + semboller
print("---Sifre Ureticisi---")
uzunluk = int(input("Sifrenizin uzunlugunu giriniz: "))
sifre = ""

for i in range(uzunluk):
    rastgele_karakter = random.choice(havuz)

    sifre = sifre + rastgele_karakter 
    print(f"sifre: {sifre}")