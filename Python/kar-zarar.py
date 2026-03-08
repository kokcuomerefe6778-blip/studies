İslemler = [150, -100, 200, 100, -50]

toplam_bakiye = 0
for durum in İslemler:
    if durum > 0:
        print("Kar: ", durum)
    else:
        print("Zarar: ", durum)

    toplam_bakiye: int = toplam_bakiye + durum

print("Bugünkü toplam bakiye: ", toplam_bakiye ,"TL")        
     