# Zadanie 3/2021 - Wagi napisów

# z d a n i e
# (1 2 3) (3 2 1) + (+1 +1 -1 +1 -1 -1) = waga_slowa

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
        lista_wag += [waga_slowa(slowo)]
    print(lista_wag)
    # return sorted(lista_slow, key=sortuj_wagi)
    return sorted(lista_slow, key=lambda slowo: (waga_slowa(slowo), slowo))

def sortuj_babelkowo_lista(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):  # Mniejszy zakres, bo po każdej iteracji elementy na końcu są posortowane
            if lista[j] > lista[j + 1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

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


lista_slow = ["basiunia", "milkamala", "ala", "krowa", "baa", "trawa"]
print(sortuj(lista_slow))
lista_slow = sorted(lista_slow, key=len)

lista = [6, 7, 17, 9, 1, 0, 12, 16]
print(lista)
sortuj_babelkowo_lista(lista)
print(lista)

# print(lista_slow)

# # wejscie = input("Podaj slowa:")
# wejscie = "ala ma kota"
# lista_slow = wejscie.split()
#
# print(sortuj(lista_slow))
# print(sortuj_babelkowo(lista_slow))

