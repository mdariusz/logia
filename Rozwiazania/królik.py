g = int(input())
dolki = list(map(int, input().split()))

suma = 0

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
    # wszystkie są >= g
    # znajdujemy najpłytszy dołek
    min_dolek = min(dolki)

    # liczymy, ile jest takich najpłytszych
    for d in dolki:
        if d == min_dolek:
            suma += min_dolek - g

print(suma)
