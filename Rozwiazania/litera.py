def litera(slowa):
    liczniki = [0 for _ in range(26)]
    for slowo in slowa:
        for litera in slowo:
            liczniki[ord(litera) - 97] += 1

    m = max(liczniki)
    if liczniki.count(m) == 1:
        return chr(97 + liczniki.index(m))
    else:
        wynik = []
        for i in range(26):
            if liczniki[i] == m:
                wynik.append(chr(97 + i))
        return wynik
