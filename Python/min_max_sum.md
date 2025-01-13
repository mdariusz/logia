## Funkcje `min()`, `max()`, `sum()` 

### 1. `min()`
Funkcja `min()` zwraca najmniejszą wartość z podanych elementów lub listy.

**Przykłady:**
```python
print(min([3, 5, 7, 2, 8]))  # 2
print(min(3, 5, 7, 2, 8))    # 2
```

### 2. `max()`
Funkcja `max()` zwraca największą wartość z podanych elementów lub listy.

**Przykłady:**
```python
print(max([3, 5, 7, 2, 8]))  # 8
print(max(3, 5, 7, 2, 8))    # 8
```

### 3. `sum()`
Funkcja `sum()` oblicza sumę elementów w liście lub krotce.

**Przykłady:**
```python
print(sum([3, 5, 7, 2, 8]))  # 25
print(sum((3, 5, 7, 2, 8)))  # 25
```

## `min()` i `max()` ze stringami

### Działanie:
- **`min()`**: Zwraca najmniejszy (leksykograficznie) znak lub słowo w stringu.
- **`max()`**: Zwraca największy (leksykograficznie) znak lub słowo w stringu.

### Przykłady:

#### `min()` ze stringiem
```python
text = "hello"
print(min(text))  # Output: 'e' (najmniejszy znak w kolejności ASCII)
```

#### `max()` ze stringiem
```python
text = "hello"
print(max(text))  # Output: 'o' (największy znak w kolejności ASCII)
```

#### `min()` i `max()` z listą słów
```python
words = ["apple", "banana", "cherry"]
print(min(words))  # Output: 'apple' (pierwsze w kolejności leksykograficznej)
print(max(words))  # Output: 'cherry' (ostatnie w kolejności leksykograficznej)
```

### Zasada:
- `min()` i `max()` działają na zasadzie porównania leksykograficznego, gdzie porównywane są kody ASCII znaków.


