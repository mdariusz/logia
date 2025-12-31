g = int(input())
dolki = list(map(int, input().split()))

suma = 0

# g = 20
# d = 8 30 15 40 20

# sprawdzamy, czy jest dołek płytszy niż g
jest_za_plytki = False
for d in dolki:
    if d < g:
        jest_za_plytki = True

if jest_za_plytki:
    # pogłębiamy tylko za płytkie dołki do g
    for d in dolki:
        if d < g:
            suma += g - d
else:
    # g = 12
    # d = 30 40 50 40 30 60 70
    # wszystkie są >= g
    # znajdujemy najpłytszy dołek
    min_dolek = min(dolki)

    # liczymy, ile jest takich najpłytszych
    for d in dolki:
        if d == min_dolek:
            suma += min_dolek - g

print(suma)
