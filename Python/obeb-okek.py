sayi1 = int(input("Birinci sayiyi giriniz: "))
sayi2 = int(input("Ikinci sayiyi giriniz: "))
enkücük = min(sayi1, sayi2)

for i in range(enkücük, 0,-1):
    if sayi1 % i == 0 and sayi2 % i == 0:
        obeb = i
        break
okek = (sayi1 * sayi2)// obeb
print(f"Obeb: {sayi1} ve {sayi2} sayilarin obebi: {obeb}")
print(f"Okek: {sayi1} ve {sayi2} sayilarin okeki: {okek}") 