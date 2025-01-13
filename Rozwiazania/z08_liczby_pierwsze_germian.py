## Zadanie 4/2024_e2 - Liczby pierwsze Germian
import math

############################################################
def drukuj_indeks_wartosc(lista_wartosci):
    for indeks, wartosc in enumerate(lista_wartosci):
        print(indeks,":", wartosc)

def zaznacz_liczby_zlozone(lista_wartosci):
    for indeks, wartosc in enumerate(lista_wartosci):
        if wartosc:
            print(indeks,"")
        else:
            print(indeks, "x")
############################################################



def czy_pierwsza(liczba):
    if liczba == 2:
        return True
    if liczba % 2 == 0:
        return False
    od = 3
    do = liczba // 2 + 1
    krok = 2
    for dzielnik in range(od, do, krok):
        if liczba % dzielnik == 0:
            return False
    return True



def czy_pierwsza_kwadrat(liczba):
    if liczba == 2:
        return True
    if liczba % 2 == 0:
        return False
    od = 3
    do = int(math.sqrt(liczba)) + 1  # użycie math.sqrt zamiast potęgowania
    krok = 2
    for dzielnik in range(od, do, krok):  # tylko liczby nieparzyste
        if liczba % dzielnik == 0:
            return False
    return True


def ile_liczb_germian():
    a, b = input("Zakres: ").split()
    a = int(a)
    b = int(b)
    ile_liczb_germian = 0
    for i in range(a, b + 1):
        if czy_pierwsza(i) and czy_pierwsza(2 * i + 1):
            ile_liczb_germian += 1
    return ile_liczb_germian


def sito(liczba):
    pierwsze = []
    for i in range(liczba + 1):
        if i % 2 == 1:
            pierwsze.append(True)
        else:
            pierwsze.append(False)

    pierwsze[1] = False
    pierwsze[2] = True

    od = 3
    do = int(math.sqrt(liczba)) + 1
    krok = 2
    for dzielnik in range(od, do, krok):
        if pierwsze[dzielnik]:
            for i in range(dzielnik * dzielnik, liczba + 1, dzielnik):
                pierwsze[i] = False
    return pierwsze


def ile_liczb_germian_sito():
    a, b = input("Zakres: ").split()
    a = int(a)
    b = int(b)

    pierwsze = sito(2 * b + 1)
    ile_liczb_germian = 0
    for i in range(a, b + 1):
        if pierwsze[i] and pierwsze[2 * i + 1]:
            ile_liczb_germian += 1
    return ile_liczb_germian



#print(czy_pierwsza(49))
#print(ile_liczb_germian())
print(ile_liczb_germian_sito())
