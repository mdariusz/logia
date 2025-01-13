## Zadanie 2/2023_e2 - Kodowanie


def koduj_samogloski(wiadomosc):
    kodowanie = ""
    samogloski = 'aeiouy'
    for samogloska in samogloski:
        ile_samoglosek = wiadomosc.count(samogloska)
        if ile_samoglosek == 1:
            kodowanie += samogloska
        elif ile_samoglosek > 1:
            kodowanie += samogloska + str(ile_samoglosek)
    return kodowanie



def koduj_spolgloski(wiadomosc):
    kodowanie = ""
    spolgloski = 'bcdfghjklmnpqrstvwxz'
    for spolgloska in spolgloski:
        ile_spolglosek = wiadomosc.count(spolgloska)
        if ile_spolglosek == 1:
            kodowanie += spolgloska
        elif ile_spolglosek > 1:
            kodowanie += spolgloska + str(ile_spolglosek)
    return kodowanie


def kodowanie():
    n = int(input("Podaj liczbę wierszy: "))
    for i in range(n):
        wiadomosc = input("Wiadomość: ")
        zakodowana_wiadomosc = koduj_samogloski(wiadomosc) + koduj_spolgloski(wiadomosc)
        print(zakodowana_wiadomosc)



wiadomosc = "aabbcccccfghju"
print(koduj_samogloski(wiadomosc))
# print(koduj_spolgloski(wiadomosc))

#kodowanie()
