def suma_cyfr(liczba):
    suma = 0
    while liczba != 0:
        suma += liczba % 10
        liczba //= 10
    return suma


def jaka(a, b, n):
    licznik = 0
    x = 1
    while x <= 100_000:
        suma = suma_cyfr(x)
        if a < suma < b:
            licznik += 1
            if licznik == n:
                return x
        x += 1
    return -1

def test():
    assert jaka(1, 3, 5) == 110

test()