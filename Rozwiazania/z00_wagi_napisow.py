# Zadanie 3/2021 - Wagi napisów


def waga_slowa(slowo):
    dlugosc_slowa = len(slowo)
    waga_slowa = 0
    for i in range(dlugosc_slowa // 2):
        waga_slowa += (i + 1) * 2
    if dlugosc_slowa % 2 == 1:
         waga_slowa += (dlugosc_slowa // 2) + 1

    for litera in slowo:
        if litera in "aeiouy":
            waga_slowa -= 1
        else:
            waga_slowa += 1
    return waga_slowa

def sortuj_wagi(slowo):
    return (waga_slowa(slowo), slowo)


def sortuj(lista_slow):
    print(lista_slow)
    lista_wag = []
    for slowo in lista_slow:
        lista_wag.append(waga_slowa(slowo))
    print(lista_wag)
    return sorted(lista_slow, key=sortuj_wagi)

def sortuj_babelkowo(lista_slow):
    n = len(lista_slow)
    for i in range(n):
        for j in range(0, n-i-1):  # Mniejszy zakres, bo po każdej iteracji elementy na końcu są posortowane
            if waga_slowa(lista_slow[j]) > waga_slowa(lista_slow[j+1]):
                # Zamiana miejscami słów
                lista_slow[j], lista_slow[j+1] = lista_slow[j+1], lista_slow[j]
            # W przypadku równych wag, sortuj leksykograficznie
            elif waga_slowa(lista_slow[j]) == waga_slowa(lista_slow[j+1]) and lista_slow[j] > lista_slow[j+1]:
                lista_slow[j], lista_slow[j+1] = lista_slow[j+1], lista_slow[j]
    return lista_slow

# wejscie = input("Podaj slowa:")
wejscie = "ala ma kota"
lista_slow = wejscie.split()

print(sortuj(lista_slow))
print(sortuj_babelkowo(lista_slow))

