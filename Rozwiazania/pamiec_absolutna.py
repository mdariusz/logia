n = int(input())
karty = list(map(int, input().split()))

pamiec = [0] * (n + 1)   # pamięć kart: 0 albo 1
ruchy = 0

for karta in reversed(karty):
    if pamiec[karta] == 1:
        # druga taka sama karta → usuwamy parę
        ruchy += 1
        pamiec[karta] = 0
    else:
        # pierwsze spotkanie karty → zapamiętujemy
        ruchy += 1
        pamiec[karta] = 1

print(ruchy)
