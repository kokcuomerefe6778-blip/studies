basinc = int(input("Lastik basincini giriniz: "))

if basinc < 0:
    print("Sensor hatasi!")
elif basinc < 28:
    print("Uyari:Lastik basinci düsük! Kontrol ediniz!")
elif basinc <= 36:
    print("Lastik basinci ideal.")
else:
    print("Lastik cok sisirilmis dikkat ediniz!")