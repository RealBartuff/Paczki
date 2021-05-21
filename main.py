
waga_paczki = 0
maks_paczka = 20
ilosc_paczek = 0
suma_kilo = 0
suma_pustych_kilo = 0

element = float(input())
while element:
    if element <= 10:
        element = float(input())
        waga_paczki += element
        print("Dodano element do paczki: {}, Akutualna waga paczki: {}".format(element, waga_paczki))
        if waga_paczki == maks_paczka:
            ilosc_paczek += 1
            print("Wysłano paczkę o wadze: {}, Wysłane paczki: {}".format(waga_paczki, ilosc_paczek))
        if waga_paczki > 20:
            print("Paczka przeciążona! Dodaję element do nowej paczki.")
            waga_paczki -= element
            ilosc_paczek += 1
            suma_kilo += waga_paczki
            suma_pustych_kilo += maks_paczka - waga_paczki
            print("Wysłano paczkę o wadze: {}, Puste kilogramy {}".format(waga_paczki, suma_pustych_kilo))
            waga_paczki = 0
            if 1 > element > 10:
                print("Nieprawidłowa waga elementu (podaj wagę z przedziału od 1 do 10 kg)")
                break
    elif element == 0:
        print("Koniec programu")
        break
    else:
        print("error")
        break

'''print("Suma wysłanych paczek: ", ilosc_paczek)
print("Suma wysłanych kilogramów: ", suma_kilo)
print("Suma pustych kilogramów: ", suma_pustych_kilo)

elif waga_paczki > 20:
    ilosc_paczek += 1
    waga_paczki -= element
    suma_pustych_kilo += maks_paczka - waga_paczki
    print("Wysłano paczkę o wadze: ", (waga_paczki - element))
    waga_paczki = element
element = float(input())
if element:
    element = float(element)'''


