## Sortowanie bąbelkowe (Bubble Sort)

**Sortowanie bąbelkowe** to jeden z najprostszych algorytmów sortowania, choć nie jest najwydajniejszy. Algorytm ten działa poprzez wielokrotne przechodzenie przez listę (lub tablicę), porównywanie sąsiednich elementów i zamienianie ich miejscami, jeśli są w niewłaściwej kolejności. Proces powtarza się, aż lista zostanie posortowana.

### Algorytm:
1. **Początkowy stan:** Mamy listę liczb, którą chcemy posortować.
2. **Pierwsza iteracja:** Przechodzimy przez listę od początku do końca. Porównujemy kolejne pary elementów (czyli elementy o indeksach `i` i `i+1`), jeśli są w niewłaściwej kolejności (czyli `lista[i] > lista[i+1]`), to zamieniamy je miejscami.
3. **Kolejne iteracje:** Po pierwszej iteracji największy element będzie na końcu listy. Następnie wykonujemy kolejne iteracje, ignorując już posortowaną część listy na końcu (na każdym etapie posortowana część rośnie).
4. **Zakończenie:** Algorytm kończy działanie, gdy w jednym przebiegu nie dokonamy żadnej zamiany, co oznacza, że lista jest posortowana.

### Złożoność:
- **Czasowa:** O(n²), gdzie `n` to liczba elementów w liście. Jest to wynik podwójnej pętli, w której każda z nich przechodzi przez elementy listy.
- **Przestrzenna:** O(1), ponieważ algorytm działa w miejscu (in-place), czyli nie wymaga dodatkowej pamięci poza samą listą.

### Przykład z tabelką:

Załóżmy, że mamy listę liczb: `[5, 3, 8, 4, 2]`.

### Krok 1: Początkowy stan
```
[5, 3, 8, 4, 2]
```

### Krok 2: Pierwsza iteracja
Porównujemy pary elementów:
- **5 i 3**: 5 > 3, więc zamieniamy miejscami.
- **5 i 8**: 5 < 8, więc nie zamieniamy.
- **8 i 4**: 8 > 4, więc zamieniamy miejscami.
- **8 i 2**: 8 > 2, więc zamieniamy miejscami.

Po pierwszej iteracji:
```
[3, 5, 4, 2, 8]  (8 jest już na właściwym miejscu)
```

### Krok 3: Druga iteracja
Ponownie porównujemy elementy, ale tym razem ostatni element (8) jest już na właściwym miejscu, więc go pomijamy:
- **3 i 5**: 3 < 5, więc nie zamieniamy.
- **5 i 4**: 5 > 4, więc zamieniamy miejscami.
- **5 i 2**: 5 > 2, więc zamieniamy miejscami.

Po drugiej iteracji:
```
[3, 4, 2, 5, 8]  (5 i 8 są już na swoich miejscach)
```

### Krok 4: Trzecia iteracja
Teraz porównujemy tylko pierwsze trzy elementy:
- **3 i 4**: 3 < 4, więc nie zamieniamy.
- **4 i 2**: 4 > 2, więc zamieniamy miejscami.

Po trzeciej iteracji:
```
[3, 2, 4, 5, 8]
```

### Krok 5: Czwarta iteracja
Porównujemy tylko pierwsze dwa elementy:
- **3 i 2**: 3 > 2, więc zamieniamy miejscami.

Po czwartej iteracji:
```
[2, 3, 4, 5, 8]
```

Teraz lista jest posortowana, ponieważ nie musimy już wykonywać żadnych zamian w kolejnych iteracjach.

### Ostateczny wynik:
```
[2, 3, 4, 5, 8]
```

### Tabelka przedstawiająca kolejne kroki:
| Iteracja | Lista po iteracji          | Uwagi                   |
|----------|----------------------------|-------------------------|
| 0        | [5, 3, 8, 4, 2]             | Początkowy stan         |
| 1        | [3, 5, 4, 2, 8]             | Zamiany: (5,3), (8,4), (8,2) |
| 2        | [3, 4, 2, 5, 8]             | Zamiany: (5,4), (5,2)   |
| 3        | [3, 2, 4, 5, 8]             | Zamiana: (3,2)          |
| 4        | [2, 3, 4, 5, 8]             | Zamiana: (3,2)          |

### Wnioski:
- Algorytm **sortowania bąbelkowego** jest łatwy do zaimplementowania, ale jego wydajność jest dość słaba (O(n²)).
- Dzięki swojej prostocie, jest często używany w edukacji, ale w praktycznych zastosowaniach rzadko jest wybierany do sortowania dużych zbiorów danych.
