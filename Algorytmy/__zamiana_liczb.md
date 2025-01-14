## Zamiana Liczb Dziesiętnych na Inne Systemy

### 1. **Zamiana Dziesiętnej na Binarną (System Dwójkowy)**
   - **Wzór**: Dziel liczbę przez 2 i zapisuj reszty.
   - **Przykład**: Zamiana $200000$ na system binarny:
     1. $200000 \div 2 = 100000$ (reszta 0)
     2. $100000 \div 2 = 50000$ (reszta 0)
     3. $50000 \div 2 = 25000$ (reszta 0)
     4. $25000 \div 2 = 12500$ (reszta 0)
     5. $12500 \div 2 = 6250$ (reszta 0)
     6. $6250 \div 2 = 3125$ (reszta 0)
     7. $3125 \div 2 = 1562$ (reszta 1)
     8. Kontynuujemy, aż iloraz wyniesie 0.

   **Wynik**: $200000_{10} = 110000110101000000_2$

### 2. **Zamiana Dziesiętnej na Ósemkową (System Ósemkowy)**
   - **Wzór**: Dziel liczbę przez 8 i zapisuj reszty.
   - **Przykład**: Zamiana $200000$ na system ósemkowy:
     1. $200000 \div 8 = 25000$ (reszta 0)
     2. $25000 \div 8 = 3125$ (reszta 0)
     3. $3125 \div 8 = 390$ (reszta 5)
     4. $390 \div 8 = 48$ (reszta 6)
     5. $48 \div 8 = 6$ (reszta 0)
     6. $6 \div 8 = 0$ (reszta 6)

   **Wynik**: $200000_{10} = 606400_8$

### 3. **Zamiana Dziesiętnej na Szesnastkową (System Szesnastkowy)**
   - **Wzór**: Dziel liczbę przez 16 i zapisuj reszty.
   - **Przykład**: Zamiana $200000$ na system szesnastkowy:
     1. $200000 \div 16 = 12500$ (reszta 0)
     2. $12500 \div 16 = 781$ (reszta 4)
     3. $781 \div 16 = 48$ (reszta 13, czyli D)
     4. $48 \div 16 = 3$ (reszta 0)
     5. $3 \div 16 = 0$ (reszta 3)

   **Wynik**: $200000_{10} = 30D40_{16}$

### 4. **Zamiana Dziesiętnej na Siódemkową (System Siódemkowy)**
   - **Wzór**: Dziel liczbę przez 7 i zapisuj reszty.
   - **Przykład**: Zamiana $200000$ na system siódemkowy:
     1. $200000 \div 7 = 28571$ (reszta 3)
     2. $28571 \div 7 = 4081$ (reszta 4)
     3. $4081 \div 7 = 583$ (reszta 0)
     4. $583 \div 7 = 83$ (reszta 2)
     5. $83 \div 7 = 11$ (reszta 6)
     6. $11 \div 7 = 1$ (reszta 4)
     7. $1 \div 7 = 0$ (reszta 1)

   **Wynik**: $200000_{10} = 1462034_7$

## Zamiana Liczb Dziesiętnych na Inne Systemy z Konkretnego Przykładu (200000)

### 1. **Zamiana Dziesiętnej na Binarną (System Dwójkowy)**
   - **Przykład dla $200000$:**
     $$
     200000 = 1 \cdot 2^{17} + 1 \cdot 2^{16} + 0 \cdot 2^{15} + 0 \cdot 2^{14} + 0 \cdot 2^{13} + 0 \cdot 2^{12} + 1 \cdot 2^{11} + 1 \cdot 2^{10} + 0 \cdot 2^9 + 1 \cdot 2^8 + 0 \cdot 2^7 + 1 \cdot 2^6 + 0 \cdot 2^5 + 0 \cdot 2^4 + 0 \cdot 2^3 + 0 \cdot 2^2 + 0 \cdot 2^1 + 0 \cdot 2^0
     $$
     **Wynik**: $110000110101000000_2$

### 2. **Zamiana Dziesiętnej na Ósemkową (System Ósemkowy)**
   - **Przykład dla $200000$:**
     $$
     200000 = 6 \cdot 8^5 + 0 \cdot 8^4 + 6 \cdot 8^3 + 4 \cdot 8^2 + 0 \cdot 8^1 + 0 \cdot 8^0
     $$
     **Wynik**: $606400_8$

### 3. **Zamiana Dziesiętnej na Szesnastkową (System Szesnastkowy)**
   - **Przykład dla $200000$:**
     $$
     200000 = 3 \cdot 16^4 + 0 \cdot 16^3 + 13 \cdot 16^2 + 4 \cdot 16^1 + 0 \cdot 16^0
     $$
     **Wynik**: $30D40_{16}$

### 4. **Zamiana Dziesiętnej na Siódemkową (System Siódemkowy)**
   - **Przykład dla $200000$:**
     $$
     200000 = 1 \cdot 7^5 + 4 \cdot 7^4 + 6 \cdot 7^3 + 2 \cdot 7^2 + 0 \cdot 7^1 + 3 \cdot 7^0
     $$
     **Wynik**: $1462034_7$

## Funkcje zamiany liczb w Pythonie

Python posiada wbudowane funkcje do konwersji liczb z systemu dziesiętnego na binarny, szesnastkowy, ósemkowy oraz odwrotnie:

1. **`bin()`** – konwertuje liczbę dziesiętną na binarną:
   ```python
   bin(10)  # '0b1010'
   ```

2. **`hex()`** – konwertuje liczbę dziesiętną na szesnastkową:
   ```python
   hex(10)  # '0xa'
   ```

3. **`oct()`** – konwertuje liczbę dziesiętną na ósemkową:
   ```python
   oct(10)  # '0o12'
   ```

4. **`int()`** – konwertuje liczbę z systemu binarnego, szesnastkowego lub ósemkowego do dziesiętnego:
   ```python
   int('1010', 2)  # 10 (binarny na dziesiętny)
   int('a', 16)    # 10 (szesnastkowy na dziesiętny)
   int('12', 8)    # 10 (ósemkowy na dziesiętny)
   ```

## Zamiana liczb o dowolnej podstawie

```python
def to_base(n, base):
    if n == 0:
        return "0"
    digits = []
    while n:
        digits.append(int(n % base))
        n //= base
    digits.reverse()  # Odwrócenie listy

    result = ""
    for x in digits:
        result += str(x)  # Łączenie elementów w ciąg znaków
    return result
 
to_base(123232,7)
```