# Zadanie 4/2021 - Liczby czterocyfrowe

# 5643 % 10 = 3
# 5643 // 10 = 564

# 564 % 10 = 4
# 564 // 10 = 56

## 56 % 10 = [6]
#  56 // 10 = 5

## 5 % 10 = [5]
##   5 // 5 = 0

# 5643 cyfry: [5, 6, 4, 3] => min:[3, 4, 5, 6] => max:[6, 5, 4, 3] => (6543 - 3456) = 1257 = 1257 = 1257
def liczba_na_lista_cyfr(liczba):
    lista_cytr = []
    while liczba > 0:
        # Pobranie ostatniej cyfry
        ostatnia_cyfra = liczba % 10
        lista_cytr = [ostatnia_cyfra] + lista_cytr
        # Usunięcie ostatniej cyfry z liczby
        liczba = liczba // 10
    return lista_cytr


# def liczba_na_lista_cyfr_str(liczba):
#     liczba_str = str(liczba)
#     lista_cyfr = []
#     for cyfra_str in liczba_str:
#         lista_cyfr.append(int(cyfra_str))
#         # lista_cyfr += [int(cyfra_str)]
#     return lista_cyfr


# Zamiana listy cyfr na liczbę
def lista_cyfr_na_liczbe(lista_cyfr):
    liczba = 0
    for cyfra in lista_cyfr:
        liczba = liczba * 10 + cyfra
    return liczba


# Generowanie następnego elementu
def roznica(liczba):
    lista_cyfr = liczba_na_lista_cyfr(liczba)
    lista_cyfr_sortowana = sorted(lista_cyfr)
    a = lista_cyfr_na_liczbe(lista_cyfr_sortowana)
    b = lista_cyfr_na_liczbe(lista_cyfr_sortowana[::-1])
    return b - a

# Generowanie, aż do stałego elementu
def generator(liczba):
    ile = 0
    x = liczba
    y = roznica(liczba)
    while x != y:
        x = y
        y = roznica(x)
        ile += 1
    return ile

#print(petla(int(input())))
# lista_cyfr = liczba_na_lista_cyfr(321653535)
# print(lista_cyfr)
# liczba = lista_cyfr_na_liczbe(lista_cyfr)
# print(liczba)
#print(roznica(1235))

liczby = [
    1111,
    9834,
    5689,
    7491,
    9998,
    3434,
    6174,
    4536,
    2887,
    2888
]

for liczba in liczby:
    print(generator(liczba))
