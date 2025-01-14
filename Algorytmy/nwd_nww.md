## NWD (największy wspólny dzielnik) 
## NWW (najmniejsza wspólna wielokrotność)


```python
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
1. **Funkcja `NWD(a, b)`**:
   - Zawiera tylko algorytm Euklidesa, który zwraca **NWD**.
   
2. **Funkcja `NWW(a, b)`**:
   - Oblicza **NWW** na podstawie wcześniej obliczonego **NWD**. Korzysta z funkcji `NWD` w celu obliczenia wspólnego dzielnika, a potem stosuje wzór:  
   $$
   \text{NWW}(a, b) = \frac{|a \times b|}{\text{NWD}(a, b)}
   $$

### Przykład działania:
Dla `a = 36` i `b = 60`:
- **NWD(36, 60)** = 12
- **NWW(36, 60)** = 180

### Podsumowanie:
Teraz funkcje są rozdzielone i obie wykonują tylko jedną odpowiedzialność: obliczanie NWD oraz NWW.