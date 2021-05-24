
waga_paczki = 0
puste_kilo = 0
maks_paczka = 20
ilosc_paczek = 0
suma_kilo = 0
suma_pustych_kilo = 0
najmniejsza_paczka = 20
nr_najmniejszej = 0
maks_puste = 0

element = float(input())
while True:
    if element == 0:
        ilosc_paczek += 1
        suma_kilo += waga_paczki
        puste_kilo += maks_paczka - waga_paczki
        suma_pustych_kilo += puste_kilo
        print("Podano element o wadze 0 kg. Koniec programu. Wszystkie elementy zostały wysłane.")
        print("Wysłano paczkę nr {}, o wadze: {}, Puste kilogramy {}".format(ilosc_paczek, waga_paczki, puste_kilo))
        if waga_paczki < najmniejsza_paczka:
            najmniejsza_paczka = waga_paczki
            maks_puste = 20 - najmniejsza_paczka
            nr_najmniejszej = ilosc_paczek
        break
    if element < 1 or element > 10:
        print("Nieprawidłowa waga elementu (podaj wagę z przedziału od 1 do 10 kg)")
        break
    waga_paczki += element
    print("Dodano element do paczki: {}, Aktualna waga paczki: {}".format(element, waga_paczki))
    if waga_paczki > 20:
        print("Paczka przeciążona! Dodaję element", element, "do nowej paczki.")
        waga_paczki -= element
        ilosc_paczek += 1
        suma_kilo += waga_paczki
        puste_kilo += maks_paczka - waga_paczki
        print("Wysłano paczkę nr {}, o wadze: {}, Puste kilogramy {}".format(ilosc_paczek, waga_paczki, puste_kilo))
        if waga_paczki < najmniejsza_paczka:
            najmniejsza_paczka = waga_paczki
            maks_puste = 20 - najmniejsza_paczka
            nr_najmniejszej = ilosc_paczek
        suma_pustych_kilo += puste_kilo
        waga_paczki = element
        puste_kilo = 0

    element = float(input())

print("Suma wysłanych paczek: ", ilosc_paczek)
print("Suma wysłanych kilogramów: ", suma_kilo)
print("Suma pustych kilogramów: ", suma_pustych_kilo)
print("Najwięcej pustych kilogramów w paczce nr {}: {}".format(nr_najmniejszej, maks_puste))
