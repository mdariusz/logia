n = int(input())
karty = list(map(int, input().split()))

pamiec = [0] * (n + 1)  # 0 = nie widziana, 1 = widziana, 2 = para zdjęta
ruchy = 0
i = 2 * n - 1

while i >= 0:
    a = karty[i]
    ruchy += 1  # ruch na pierwszej karcie

    if pamiec[a] == 1:
        # druga karta już była widziana → zbieramy parę
        pamiec[a] = 2
        i -= 1
    else:
        # pierwsze spotkanie → odkrywamy drugą kartę w tym ruchu
        pamiec[a] = 1
        if i - 1 >= 0:
            b = karty[i - 1]
            if pamiec[b] == 1:
                # druga karta była już widziana → dodatkowy ruch
                ruchy += 1
                pamiec[b] = 2
            elif pamiec[b] == 0:
                pamiec[b] = 1  # zapamiętujemy
        i -= 2

print(ruchy)
