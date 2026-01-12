# 0
# 1   2
# 3   4   5
# 6   7   8   9
# 10 11  12  13

def kolit(slowo):
    # tworzenie wierszy
    wiersze = []
    i = 0
    dlugosc_wiersza = 1
    while i < len(slowo):
        wiersz = []
        for _ in range(dlugosc_wiersza):
            if i < len(slowo):
                wiersz.append(slowo[i])
                i += 1
        wiersze.append(wiersz)
        dlugosc_wiersza += 1
    print("Wiersze:", wiersze)

    # transpozycja: kolumny tworzymy w locie
    kolumny = []
    for w in wiersze:
        for i in range(len(w)):
            if i == len(kolumny):
                kolumny.append([])   
            kolumny[i].append(w[i]) 
    print("Kolumny:", kolumny)

    # proste sprawdzenie jednolitych kolumn
    licznik_kolumn = 0
    for kol in kolumny:
        jednolita = True
        for l in kol:
            if l != kol[0]:
                jednolita = False
                break
        if jednolita:
            licznik_kolumn += 1

    print("Liczba jednolitych kolumn:", licznik_kolumn)

kolit('ALAMAKRABY')
