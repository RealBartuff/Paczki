
waga_paczki = 0
ilosc_paczek = 0
ilosc_elementow = 0
maks_paczka = 20
suma_kilo = 0
suma_pustych_kilo = 0

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
            ilosc_paczek += 1
            waga_paczki -= element
            suma_pustych_kilo += maks_paczka - waga_paczki
            print("Wysłano paczkę o wadze: ", (waga_paczki - element))
            waga_paczki = element
        element = input()
        if element:
            element = int(element)
    else:
        print("Element za ciężki: ", element)
        break
print("ilosc paczek: ", ilosc_paczek)

if suma_kilo > 0:
    ilosc_paczek += 1

"""
if element == 0:
    print("Koniec programu")

else:
    print("Za duża waga elementu")

    
"""

