hiz = 0
vites = 0

print("Hizlaniliyor...")

while hiz < 120:
    hiz = hiz + 20

    if hiz > 0 and hiz <=30:
        vites = 1 
    elif hiz > 30 and hiz <= 60:
        vites = 2   
    elif hiz > 60 and hiz <= 90:
        vites = 3
    elif hiz > 90 and hiz <= 120:
        vites = 4      
    print("Hiz:" , hiz, "km/h", "Vites: ", vites)      
    print("Yavaslaniyor...")