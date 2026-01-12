# Zadanie 4/2022 - Szyfr kolumnowy


# Funkcja budująca klucz na podstawie porządku liter w kluczu
def budowanie_klucza(klucz):
    klucz_sortowany = sorted(list(klucz))  # Posortowany klucz
    print(klucz_sortowany)
    kolumny = []
    for x in klucz:
        i = klucz_sortowany.index(x)
        klucz_sortowany[i] = '*'
        kolumny.append(i)
    print(kolumny)
    return kolumny

def szyfr_kolumnowy(wiadomosc, klucz):
    szyfr = ""

    # Budowanie klucza
    kolumny = budowanie_klucza(klucz)


    klucz_dlugosc = len(klucz)
    wiadomosc_dlugosc = len(wiadomosc)


    # Iterujemy przez każdą kolumnę w porządku określonym przez klucz
    for i in range(klucz_dlugosc):
        j = kolumny[i]
        while j < wiadomosc_dlugosc:
            szyfr += wiadomosc[j]
            j += klucz_dlugosc  # Przechodzimy do kolejnego znaku w tej samej kolumnie
    return szyfr



# wiadomosc, klucz = input().split()
# Przykładowe dane wejściowe
wiadomosc = "konkurslogia"
klucz = "oczko"

wiadomosc = "tajnawiadomosc"
klucz = "plot"

wiadomosc = "spotkanieodwolane"
klucz = "kajak"



print(szyfr_kolumnowy(wiadomosc, klucz))

