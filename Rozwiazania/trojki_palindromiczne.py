def czy_pali(x):
    return str(x) == str(x)[::-1]


def pali(liczba):
    # tworzenie listy liczb palindromicznych
    pom = []
    for i in range(1, liczba + 1):
        if czy_pali(i):
            pom.append(i)

    # sprawdzanie trójek liczb
    ile = 0
    for i in range(len(pom)):
        for j in range(i + 1, len(pom)):
            x = pom[i]
            y = pom[j]
            z = liczba - x - y
            if z > y and z in pom:
                ile += 1

    return ile

