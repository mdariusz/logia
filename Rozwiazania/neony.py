def neon(slupy):
    n = len(slupy)
    best = 0

    for i in range(n):
        for j in range(i + 1, n):
            print((i,j))
            odleglosc = (j - i) * 2
            ocena = slupy[i] + slupy[j] + odleglosc
            if ocena > best:
                best = ocena

    return best


wynik = neon([10, 4, 5, 7, 1, 4, 1])
print(wynik)