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

## Algorytmy NWD i NWW na przykładzie *a = 36* i *b = 60*

### 1. Algorytm NWD (Największy wspólny dzielnik)

**Krok 1:**\
`a, b = b, a % b`

Wejście: `a = 36`, `b = 60`.\
Obliczamy `a % b`: - `b = 36 % 60 = 36` (ponieważ 36 jest mniejsze od
60).

**Krok 2:**\
`a, b = b, a % b`

Teraz `a = 60`, `b = 36`.\
Obliczamy `a % b`: - `b = 60 % 36 = 24`.

**Krok 3:**\
`a, b = b, a % b`

Teraz `a = 36`, `b = 24`.\
Obliczamy `a % b`: - `b = 36 % 24 = 12`.

**Krok 4:**\
`a, b = b, a % b`

Teraz `a = 24`, `b = 12`.\
Obliczamy `a % b`: - `b = 24 % 12 = 0`.

**Krok 5:**

Ponieważ `b = 0`, algorytm kończy się, a ostatnie niezerowe `a` to 12.\
**Wynik NWD(36, 60) = 12**.

### 2. Algorytm NWW (Najmniejsza wspólna wielokrotność)

**Krok 1:**\
Korzystamy ze wzoru:\

![ NWW(a, b) = \\frac{\|a \\times b\|}{NWD(a, b)} ](https://latex.codecogs.com/png.latex?%20NWW%28a%2C%20b%29%20%3D%20%5Cfrac%7B%7Ca%20%5Ctimes%20b%7C%7D%7BNWD%28a%2C%20b%29%7D%20 " NWW(a, b) = \frac{|a \times b|}{NWD(a, b)} ")

**Krok 2:**\
Mając NWD(36, 60) = 12, obliczamy:

![ NWW(36, 60) = \\frac{\|36 \\times 60\|}{12} ](https://latex.codecogs.com/png.latex?%20NWW%2836%2C%2060%29%20%3D%20%5Cfrac%7B%7C36%20%5Ctimes%2060%7C%7D%7B12%7D%20 " NWW(36, 60) = \frac{|36 \times 60|}{12} ")

**Krok 3:**\
Obliczenia: - \$ 36 `\times 60`{=tex} = 2160 \$ - \$
`\frac{2160}{12}`{=tex} = 180 \$

**Wynik NWW(36, 60) = 180**.

### Podsumowanie:

-   **NWD(36, 60) = 12**
-   **NWW(36, 60) = 180**

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
