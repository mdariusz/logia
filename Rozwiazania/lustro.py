def czy_palindrom(liczba):
    return str(liczba) == str(liczba)[::-1]


def l2(liczba):
    return int(str(liczba)[::-1])


def lustro(liczba, n):
    i = 0
    nowa = liczba + l2(liczba)
    while i < n:
        if czy_palindrom(nowa):
            return nowa
        else:
            nowa = nowa + l2(nowa)
            i += 1
    return -1
