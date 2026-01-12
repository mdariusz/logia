## Funkcja suma_cyfr

```python
def suma_cyfr(n):
    pom = 0
    while n > 0:
        pom += n % 10  # Dodanie ostatniej cyfry do sumy
        n = n // 10  # Usunięcie ostatniej cyfry z liczby
    return pom

print(suma_cyfr(4))  # Wynik: 10
```


## Suma kolejnych liczb

```python
def suma(n):
    s = 0
    for i in range(n):
        s = s + i
    return s

print(suma(6))

```


## Suma liczb z przedziału
```python
def suma_przedzial(a, b):
    s = 0
    for i in range(a, b + 1):  # Uwzględnienie końcowej wartości b
        s += i
    return s

print(suma_przedzial(3, 6))  # Wynik: 3 + 4 + 5 + 6 = 18

```


## Suma  cyfr

```python
def suma_cyfr(n):
    pom = 0
    while n > 0:
        pom += n % 10  # Dodanie ostatniej cyfry do sumy
        n = n // 10  # Usunięcie ostatniej cyfry z liczby
    return pom

print(suma_cyfr(1234))  # Wynik: 10
```

### Wyjaśnienie działania:

1. **Zadanie**: Funkcja oblicza sumę cyfr liczby całkowitej `n`.
2. **Przebieg pętli**:
    - `n % 10`: Wyciąga ostatnią cyfrę liczby `n`.
    - `pom += n % 10`: Dodaje tę cyfrę do zmiennej `pom`, która przechowuje sumę cyfr.
    - `n = n // 10`: Usuwa ostatnią cyfrę, dzieląc liczbę całkowitoliczbowo przez 10.
3. **Zwracanie wyniku**: Po zakończeniu pętli, `pom` zawiera sumę wszystkich cyfr.

### Wynik dla przykładu:

- Dla `n = 1234`:
    1. `1234 % 10 = 4`, `pom = 4`, `n = 123`.
    2. `123 % 10 = 3`, `pom = 7`, `n = 12`.
    3. `12 % 10 = 2`, `pom = 9`, `n = 1`.
    4. `1 % 10 = 1`, `pom = 10`, `n = 0`.

### Wartości zwrócone:

- `suma_cyfr(1234)` → 10.


## Suma cyfr nieparzystych
`
```python
def suma_cyfrp(n):
    pom = 0
    while n > 0:
        cyfra = n % 10  # Wyodrębnienie ostatniej cyfry
        if cyfra % 2 == 1:  # Sprawdzenie, czy cyfra jest nieparzysta
            pom += cyfra  # Dodanie nieparzystej cyfry do sumy
        n //= 10  # Usunięcie ostatniej cyfry z liczby
    return pom

print(suma_cyfrp(1234))  # Wynik: 1 + 3 = 4

```

## Suma cyfr parzystych

```python
def suma_cyfrp(n):
    pom = 0
    while n > 0:
        cyfra = n % 10  # Wyodrębnienie ostatniej cyfry
        if cyfra % 2 == 0:  # Sprawdzenie, czy cyfra jest nieparzysta
            pom += cyfra  # Dodanie nieparzystej cyfry do sumy
        n //= 10  # Usunięcie ostatniej cyfry z liczby
    return pom

print(suma_cyfrp(1234))  # Wynik: 1 + 3 = 4

```

## Zamiana listy cyfr na liczbę w Pythonie


### 1. Metoda matematyczna

```python
digits = [1, 2, 3, 4]
num = 0
for d in digits:
    num = num * 10 + d
print(num)  # 1234
```

### 2. Metoda z `join` i `int`

```python
digits = [1, 2, 3, 4]
num = int(''.join(map(str, digits)))
print(num)  # 1234
```

```
