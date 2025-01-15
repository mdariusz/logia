# Zadanie 4/2022 - Szyfr kolumnowy


# Funkcja budująca klucz na podstawie porządku liter w kluczu
def budowanie_klucza(klucz):
    klucz_sortowany = sorted(list(klucz))  # Posortowany klucz
    kolumny = []
    for x in klucz:
        i = klucz_sortowany.index(x)  # Znalezienie indeksu litery w posortowanym kluczu
        kolumny.append(i)  # Dodanie indeksu do listy kolumn
        klucz_sortowany[i] = '*'  # Oznaczenie użytej litery jako odwiedzonej
    return kolumny

def szyfr_kolumnowy(wiadomosc, klucz):
    szyfr = ""

    # Budowanie klucza
    kolumny = budowanie_klucza(klucz)

    # Szyfrowanie kolumnowe z użyciem `for`
    klucz_dlugosc = len(klucz)
    wiadomosc_dlugosc = len(wiadomosc)

    # Iterujemy przez każdą kolumnę w porządku określonym przez klucz
    for i in range(klucz_dlugosc):
        indeks_kolumny = kolumny[i]  # Indeks kolumny w oryginalnej wiadomości
        # Iteracja co `dlugosc` pozycji zaczynając od `x`
        for j in range(indeks_kolumny, wiadomosc_dlugosc, klucz_dlugosc):
            szyfr +=wiadomosc[j]
    return szyfr


# wiadomosc, klucz = input().split()
# Przykładowe dane wejściowe
wiadomosc = "konkurslogia"
klucz = "oczko"

print(szyfr_kolumnowy(wiadomosc, klucz))

