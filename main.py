
waga_paczki = 0
ilosc_paczek = 0
ilosc_elementow = 0
maks_paczka = 20

element = int(input())
while element:
    if element <= 10:
        print("Dodano element do paczki: ", element)
        ilosc_elementow += 1
        print("Elementy w paczce: ", ilosc_elementow)
        waga_paczki += element
        if waga_paczki == 20:
            print("Aktualna waga paczki: ", waga_paczki)
            print("Wysłano paczkę o wadze: ", waga_paczki)
        elif waga_paczki > 20:
            print("Wysłano paczkę o wadze: ", (waga_paczki - element))
        elif waga_paczki < 20:
            waga_paczki += element
        element = int(input())
    else:
        print("Element za ciężki: ", element)
        break


"""
if element == 0:
    print("Koniec programu")

else:
    print("Za duża waga elementu")
    
"""