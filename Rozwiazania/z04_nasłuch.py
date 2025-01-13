# Zadanie 2/2022 - Nasłuch

# U, W = input(), input().split()

U = "aaaaagggbbbzz"
W = "aabbbaaabbbcccy"


def litery_wow(sygnal_1, sygnal_2):
    # litery_sygnal = [0] * 26
    litery_sygnal_wow = []
    for i in range(26):
        litery_sygnal_wow.append(0)

    min_dlugosc = min(len(sygnal_1), len(sygnal_2))
    for indeks in range(min_dlugosc):
        litera_w_sygnale_1 = sygnal_1[indeks]
        litera_w_sygnale_2 = sygnal_2[indeks]
        if litera_w_sygnale_1 == litera_w_sygnale_2:
            indeks_litery = ord(litera_w_sygnale_1) - ord('a')
            litery_sygnal_wow[indeks_litery] += 1
    return litery_sygnal_wow



def litery_ooo(sygnal):
    # litery_sygnal = [0] * 26
    litery_sygnal = []
    for i in range(26):
        litery_sygnal.append(0)

    for indeks_litera in range(26):
        litera = chr(indeks_litera+ ord('a'))
        litery_sygnal[indeks_litera] = sygnal.count(litera)
    return litery_sygnal # [....]


def litery_ooo_1(sygnal):
    # litery_sygnal = [0] * 26
    litery_sygnal = []
    for i in range(26):
        litery_sygnal.append(0)

    for litera in sygnal:
        indeks_litera = ord(litera) - ord('a')
        litery_sygnal[indeks_litera] += 1
    return litery_sygnal


print(litery_ooo(U))
print(litery_ooo(W))




# lista_wow = litery_wow(U, W)
# lista_ooo_1 = litery_ooo(U)
# lista_ooo_2 = litery_ooo(W)
#
# lista_ooo_1 = litery_ooo_1(U)
# lista_ooo_2 = litery_ooo_1(W)
#
# print("wow:", lista_wow)
# print(lista_ooo_1)
# print(lista_ooo_2)
#
# trafienia_wow = 0
# trafienia_ooo = 0
#
for i in range(26):
    trafienia_wow += lista_wow[i]
    trafienia_ooo += min(lista_ooo_1[i], lista_ooo_2[i]) - lista_wow[i]

wynik = (trafienia_wow * 10) + trafienia_ooo
print(wynik)


