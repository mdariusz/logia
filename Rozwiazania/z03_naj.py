## Zadanie 3/2024_e2 - Naj...


alfabet = "aąbcćdeęfghijklłmnńoóprsśtuwyzźż"


def zapisz_alfabet_do_listy():
    lista_alfabet = []
    for litera in alfabet:
        lista_alfabet.append(litera)
    return lista_alfabet


def ktora_litera(litera):
    alfabet_lista = zapisz_alfabet_do_listy()
    return alfabet_lista.index(litera)


def ktora_litera_2(litera):
    alfabet_lista = zapisz_alfabet_do_listy()
    for indeks, litera_alfabetu in enumerate(alfabet_lista):
        print(indeks, litera_alfabetu)
        if litera == litera_alfabetu:
            return indeks



def ktora_litera_3(litera):
    alfabet_lista = zapisz_alfabet_do_listy()
    indeks = 0
    for litera_alfabetu in alfabet_lista:
        if litera == litera_alfabetu:
            return indeks
        indeks += 1



def znajdz(napis):
    lista_ktora_litera = []
    for litera in napis:
        lista_ktora_litera.append(ktora_litera(litera))
    print(lista_ktora_litera)

    najmniejszy_indeks_litery = min(lista_ktora_litera)
    najwiekszy_indeks_litery = max(lista_ktora_litera)
    roznica = najwiekszy_indeks_litery - najmniejszy_indeks_litery
    print(najmniejszy_indeks_litery)
    print(najwiekszy_indeks_litery)
    print("-"*30)

    return alfabet[najmniejszy_indeks_litery] + " " + alfabet[najwiekszy_indeks_litery] + " " + str(roznica)

def znajdz_logia(napis):
    alfabet = "aąbcćdeęfghijklłmnńoóprsśtuwyzźż"
    lista = [alfabet.index(x) for x in napis]
    p = min(lista)
    k = max(lista)
    return alfabet[p], alfabet[k], k - p


# mala_list = [24, 111.24, 12, 14, 1]
# print(max(mala_list))

napis = "abrakadabra"
print(znajdz(napis))



# slowa = ["ala", "ala","ala", "ala", "kot", "kot", "lis", "ala", "kot"]
# print(slowa.index("kot"))
# indeks = 1
# slowo = "word"
# krotka = (indeks, slowo)

# ind, slo = krotka
# print(krotka)

# print(ind)
# print(slo)

# alfabet_lista = zapisz_alfabet_do_listy()
# for indeks, litera in enumerate(alfabet_lista):
#    print(indeks, litera)

#napis = ""
#alfabet = "aąbcćdeęfghijklłmnńoóprsśtuwyzźż"
#lista = [alfabet.index(x) for x in napis]
#print(lista)

# print(ktora_litera("ż"))
# print(ktora_litera_2("ż"))
# print(ktora_litera_3("ż"))
# print(znajdz("księżyc"))

# print(znajdz_logia("księżyc"))

# napis = input("Podaj napis: ")
# wynik = znajdz(napis)
# print(wynik[0], wynik[1], wynik[2])

