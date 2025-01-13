## Rekurencja

```python
def silnia(n):
    if n == 0 or n == 1:  # Warunek bazowy
        return 1
    return n * silnia(n - 1)  # Rekurencyjne wywołanie

print(silnia(5))  # Wynik: 120
```

**Wyjaśnienie:**

Dla n = 5:
5 * silnia(4) → 4 * silnia(3) → 3 * silnia(2) → 2 * silnia(1) → 1.
Wynik: 120.

```python
def suma_liczb(a, b):
    if a > b:  # Warunek bazowy (jeśli zakres jest pusty)
        return 0
    return a + suma_liczb(a + 1, b)  # Dodaj bieżącą liczbę i wywołaj dla kolejnej

print(suma_liczb(1, 5))  # Wynik: 1 + 2 + 3 + 4 + 5 = 15
```

**Wyjaśnienie:**

Dla a = 1 i b = 5:
1 + suma_liczb(2, 5) → 2 + suma_liczb(3, 5) → 3 + suma_liczb(4, 5) → 4 + suma_liczb(5, 5) → 5 + suma_liczb(6, 5) → 0.


