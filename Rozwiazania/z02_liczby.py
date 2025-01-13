## Zadanie 2/2020_e2 - Liczby

def rozbij_na_cyfry(liczba):
    lista_cyfr = []
    while liczba > 0:
        cyfra = liczba % 10
        lista_cyfr.append(cyfra)
        liczba = (liczba // 10)
    return lista_cyfr


def suma(liczba):
    lista_cyfr = rozbij_na_cyfry(liczba)
    suma_pomoc = 0
    for cyfra in lista_cyfr:
        suma_pomoc = suma_pomoc + cyfra
    return suma_pomoc

def iloczyn(liczba):
    lista_cyfr = rozbij_na_cyfry(liczba)
    iloczyn_pomoc = 1
    for cyfra in lista_cyfr:
        iloczyn_pomoc = iloczyn_pomoc * cyfra
    return iloczyn_pomoc

###########################################################################
def ile(lista_liczb):
    licznik = 0
    for liczba in lista_liczb:
        if suma(liczba) == iloczyn(liczba):
            licznik += 1
            print("[{}]".format(liczba))
    return licznik



lista_testowa_1 =  [512, 4121, 1234, 1124, 36, 45, 123, 4121]

lista_testowa_2 = [237, 1412, 2141, 1142, 213, 456, 1421, 7890, 123, 2114, 22, 4121, 312, 9, 4112, 7, 1214, 8, 6790,
231, 1241, 2411, 321, 1124, 132]

print("ile =", ile(lista_testowa_1))
print("-"*20)
print("ile =", ile(lista_testowa_2))




