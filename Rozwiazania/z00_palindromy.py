# Zadanie 4/2020 - Palindrom

def czy_palindrom(napis):
    return napis == napis[::-1]


# def rozszerz_napis(napis, ile):
#     return napis + (napis[:ile])[::-1]


def rozszerz_napis(napis, ile):
    # Tworzymy fragment napisu, który chcemy odwrócić
    czesc_do_odwrocenia = napis[:ile]

    # Odwracamy fragment napisu
    odwrocony_fragment = czesc_do_odwrocenia[::-1]

    # Łączymy oryginalny napis z odwróconym fragmentem
    wynik = napis + odwrocony_fragment

    # Zwracamy wynik
    return wynik


def roz(napis):
    dlugosc_napisu = len(napis)
    for i in range(dlugosc_napisu):
        x = rozszerz_napis(napis, i)
        y = rozszerz_napis(napis[::-1], i)

        jest_palindromem_x = czy_palindrom(x)
        jest_palindromem_y = czy_palindrom(y)

        if jest_palindromem_x and not jest_palindromem_y:
            return x
        if not jest_palindromem_x and jest_palindromem_y:
            return y
        if jest_palindromem_x and jest_palindromem_y:
            if x < y:
                return x
            else:
                return y
    return -1

print(roz("zzzxyxyxy"))
print(roz("kajak"*4))

print(roz("muza"))
print(roz("muza"*4))