from math import sqrt

def czy_liczba_janka(liczba):
    if liczba <= 3:
        return False
    lista_dzielnikow = []
    for i in range(1,liczba//2 +1):
        if liczba % i == 0:
            lista_dzielnikow.append(i)
    print(lista_dzielnikow)
    if len(lista_dzielnikow) <= 1:
        return False
    srednia_arytmetyczna = sum(lista_dzielnikow)/len(lista_dzielnikow)
    pierwiastek_kwadratowy = sqrt(liczba) 
    return srednia_arytmetyczna <= pierwiastek_kwadratowy

wejscie = int(input())
sprawdzac = wejscie + 1
licznik_liczb = []

czy_liczba_janka(40)


while len(licznik_liczb) <= 5:
    if czy_liczba_janka(sprawdzac):
        licznik_liczb.append(sprawdzac)
    sprawdzac += 1
print(licznik_liczb[0],licznik_liczb[1],
      licznik_liczb[2],licznik_liczb[3],
      licznik_liczb[4])
