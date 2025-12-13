# Zadanie 3/2022 - Liczby Janka
import math

def czy_liczba_janka(liczba):
    if liczba <= 3:
        return False

    dzielniki = []
    for i in range(1, liczba):
        if liczba % i == 0:
            dzielniki.append(i)

    if len(dzielniki) <= 1:   # liczba pierwsza
        return False

    srednia = sum(dzielniki) / len(dzielniki)
    pierwiastek = math.sqrt(liczba)
    return srednia <= pierwiastek


def czy_liczba_janka_2(liczba):
    if liczba <= 3:
        return False

    dzielniki = [1]  # dodajemy 1 ręcznie
    limit = int(math.sqrt(liczba))

    for i in range(2, limit + 1):
        if liczba % i == 0:
            dzielniki.append(i)
            j = liczba // i
            if j != i:
                dzielniki.append(j)

    if len(dzielniki) <= 1:  # liczba pierwsza
        return False

    srednia = sum(dzielniki) / len(dzielniki)
    return srednia <= math.sqrt(liczba)



liczba = int(input("Podaj liczbę: "))
ile = 0
while ile < 5:
    liczba += 1
    if czy_liczba_janka(liczba):
        ile += 1
        print(liczba, end=" ")

