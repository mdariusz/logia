# Zadanie 3/2022 - Liczby Janka

def czy_liczba_janka(liczba):
    dzielniki = []
    for i in range(1, liczba):
        if liczba % i == 0:
            dzielniki.append(i)
    suma = sum(dzielniki)
    if len(dzielniki) < 2:
        return False
    else:
        return suma * suma <= len(dzielniki) * len(dzielniki) * liczba

def czy_liczba_janka_optymalna(liczba):
    dzielniki = [1]
    i = 2
    while i * i < liczba:
        if liczba % i == 0:
            dzielniki = dzielniki + [i] + [liczba // i]
        i += 1
    if i * i == liczba:
        dzielniki = dzielniki + [i]
    suma = sum(dzielniki)
    if len(dzielniki) < 2:
        return False
    else:
        return suma * suma <= len(dzielniki) * len(dzielniki) * liczba

liczba = int(input("Podaj liczbę: "))
ile = 0
while ile < 5:
    liczba += 1
    if czy_liczba_janka(liczba):
        ile += 1
        print(liczba, end=" ")

