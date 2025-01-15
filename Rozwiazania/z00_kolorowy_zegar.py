# Zadanie 2/2024 - Kolorowy zegar


def podaj_kolor_godziny(godzina):
    kolory_godzina = "cznf"  # 4 elementy
    indeks = godzina % 4
    return kolory_godzina[indeks]

def podaj_kolor_minuty(minuta):
    kolory_minuta = "znfcp"  # 5 elementów
    indeks = minuta % 5
    return kolory_minuta[indeks]

def kolorowy_zegar():
    godzina, minuta = input("Podaj czas: ").split()
    godzina = int(godzina)
    minuta = int(minuta)

    licznik_minut = 0
    while podaj_kolor_godziny(godzina) != podaj_kolor_minuty(minuta):
        licznik_minut += 1
        minuta = (minuta + 1) % 60
        if minuta == 0:
            godzina += 1
    return licznik_minut

print(kolorowy_zegar())
