## Działania

```python
print(3 + 2)
print(3 - 2)
print(3 * 2)
print(3 / 2.0) #dzielenie
print(3 // 2) #dzielenie całkowite
print(3 % 2) #reszta z dzielenia
print(3 ** 2) #potęgowanie
```

## Funkcje matematyczne
Ponadto można korzystać z funkcji z modułu math. Trzeba go jednak wcześniej zaimportować. Można importować pojedynczą funkcję from math import sqrt, bądź cały moduł `from math import *`. Wszystkie dostępne funkcje znajdziemy w [pomocy dla języka Python](https://docs.python.org/3/library/math.html)


```python
from math import *
print(sqrt(2)) #pierwiastek kwadratowy
print(factorial(4)) #silnia
print(floor(2.3)) #podłoga - największa liczba całkowita, która jest równa lub mniejsza od danej
print(ceil(2.3)) #sufit - najmniejsza liczba całkowita, która jest równa lub większa od danej
print(pi) #liczba pi
```


## Funkcje `lcm()` i `gcd()` w module `math`

### 1. **`gcd(a, b)`** - Największy wspólny dzielnik (GCD)
Zwraca największy wspólny dzielnik dwóch liczb.

```python
import math
result = math.gcd(12, 15)
print(result)  # 3
```

**Opis:** Największy wspólny dzielnik (GCD) to największa liczba, która dzieli obie liczby.

### 2. **`lcm(a, b)`** - Najmniejsza wspólna wielokrotność (LCM)
Zwraca najmniejszą wspólną wielokrotność dwóch liczb.

```python
import math
result = math.lcm(12, 15)
print(result)  # 60
```

**Opis:** Najmniejsza wspólna wielokrotność (LCM) to najmniejsza liczba, która jest wielokrotnością obu liczb.

### 3. **`round(liczba, precyzja)`** - Funkcja ta zaokrągla liczbę
Funkcja ta zaokrągla liczbę do określonej liczby miejsc po przecinku (domyślnie do najbliższej liczby całkowitej, jeśli drugi argument nie jest podany).


```python
result = round(3.14159, 2)
print(result)  # 3.14
```

