n = int(input())
karty = list(map(int, input().split()))

# 0 – nie widziana, 1 – widziana (zapamiętana), 2 – para zdjęta
pamiec = [0] * (n + 1)

ruchy = 0
i = 2 * n - 1   # zaczynamy od końca

while i >= 0:
    a = karty[i]
    ruchy += 1          # odkrycie pierwszej karty

    if pamiec[a] == 1:
        # druga karta już była zapamiętana → para zdjęta
        pamiec[a] = 2
        i -= 1
    else:
        # pierwsze spotkanie tej liczby
        pamiec[a] = 1

        b = karty[i - 1]    # druga karta w tym ruchu
        if pamiec[b] == 1:
            # była zapamiętana → zdejmujemy parę
            ruchy += 1
            pamiec[b] = 2
        else:
            pamiec[b] = 1  # zapamiętujemy

        i -= 2

print(ruchy)
