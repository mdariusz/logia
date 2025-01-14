## NWD (największy wspólny dzielnik)

## NWW (najmniejsza wspólna wielokrotność)

``` python
# Funkcja do obliczenia NWD (Największy wspólny dzielnik)
def NWD(a, b):
    while b != 0:
        a, b = b, a % b
    return a  # Zwraca NWD

# Funkcja do obliczenia NWW (Najmniejsza wspólna wielokrotność)
def NWW(a, b):
    nwd = NWD(a, b)  # Obliczamy NWD
    return abs(a * b) // nwd  # Obliczamy NWW na podstawie wzoru

# Przykładowe użycie
a = 36
b = 60
nwd = NWD(a, b)
nww = NWW(a, b)

print(f'NWD({a}, {b}) = {nwd}')
print(f'NWW({a}, {b}) = {nww}')
```

### Co się zmieniło:

1.  **Funkcja `NWD(a, b)`**:
    -   Zawiera tylko algorytm Euklidesa, który zwraca **NWD**.
2.  **Funkcja `NWW(a, b)`**:
    -   Oblicza **NWW** na podstawie wcześniej obliczonego **NWD**.
        Korzysta z funkcji `NWD` w celu obliczenia wspólnego dzielnika,
        a potem stosuje wzór:\

        ![
        \\text{NWW}(a, b) = \\frac{\|a \\times b\|}{\\text{NWD}(a, b)}
        ](https://latex.codecogs.com/png.latex?%0A%5Ctext%7BNWW%7D%28a%2C%20b%29%20%3D%20%5Cfrac%7B%7Ca%20%5Ctimes%20b%7C%7D%7B%5Ctext%7BNWD%7D%28a%2C%20b%29%7D%0A "
        \text{NWW}(a, b) = \frac{|a \times b|}{\text{NWD}(a, b)}
        ")

### Przykład działania:

Dla `a = 36` i `b = 60`: - **NWD(36, 60)** = 12 - **NWW(36, 60)** = 180

### Podsumowanie:

Teraz funkcje są rozdzielone i obie wykonują tylko jedną
odpowiedzialność: obliczanie NWD oraz NWW.

## Funkcje `lcm()` i `gcd()` w module `math`

### 1. **`gcd(a, b)`** - Największy wspólny dzielnik (GCD)

Zwraca największy wspólny dzielnik dwóch liczb.

``` python
import math
result = math.gcd(12, 15)
print(result)  # 3
```

**Opis:** Największy wspólny dzielnik (GCD) to największa liczba, która
dzieli obie liczby.

### 2. **`lcm(a, b)`** - Najmniejsza wspólna wielokrotność (LCM)

Zwraca najmniejszą wspólną wielokrotność dwóch liczb.

``` python
import math
result = math.lcm(12, 15)
print(result)  # 60
```

**Opis:** Najmniejsza wspólna wielokrotność (LCM) to najmniejsza liczba,
która jest wielokrotnością obu liczb.
