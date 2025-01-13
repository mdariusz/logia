## Operacje na listach w Pythonie

### 1. **append()**
Dodaje element na końcu listy.

```python
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # [1, 2, 3, 4]
```

### 2. **clear()**
Usuwa wszystkie elementy z listy.

```python
my_list = [1, 2, 3]
my_list.clear()
print(my_list)  # []
```

### 3. **copy()**
Tworzy kopię listy.

```python
my_list = [1, 2, 3]
copy_list = my_list.copy()
print(copy_list)  # [1, 2, 3]
```

### 4. **count()**
Zwraca liczbę wystąpień elementu w liście.

```python
my_list = [1, 2, 2, 3, 2]
print(my_list.count(2))  # 3
```

### 5. **extend()**
Dodaje elementy z innej listy na końcu listy.

```python
my_list = [1, 2]
my_list.extend([3, 4])
print(my_list)  # [1, 2, 3, 4]
```

### 6. **index()**
Zwraca indeks pierwszego wystąpienia elementu w liście.

```python
my_list = [1, 2, 3]
print(my_list.index(2))  # 1
```

### 7. **insert()**
Wstawia element na określoną pozycję w liście.

```python
my_list = [1, 2, 3]
my_list.insert(1, 'a')
print(my_list)  # [1, 'a', 2, 3]
```



### 8. **pop()**
- Usuwa element z listy na określonym indeksie i zwraca ten element.
- Jeśli nie podasz indeksu, usunięty zostanie ostatni element.

```python
my_list = [1, 2, 3]
removed_item = my_list.pop(1)
print(removed_item)  # 2
print(my_list)  # [1, 3]
```

### 9. **remove()**
- Usuwa pierwsze wystąpienie elementu z listy.
- Jeśli element nie istnieje w liście, podnosi wyjątek `ValueError`.

```python
my_list = [1, 2, 3, 2]
my_list.remove(2)
print(my_list)  # [1, 3, 2]
```


### 10. **reverse()**
Odwraca kolejność elementów w liście.

```python
my_list = [1, 2, 3]
my_list.reverse()
print(my_list)  # [3, 2, 1]
```

## 10A. `reversed()` i `[::-1]`
- `reversed()`: Zwraca odwrócony iterator.
- `[::-1]`: Odwraca sekwencję.

### Przykład `reversed()`:
```python
numbers = [1, 2, 3, 4, 5]
reversed_numbers = list(reversed(numbers))
print(reversed_numbers)  # Output: [5, 4, 3, 2, 1]
```

### Przykład `[::-1]`:
```python
text = "hello"
reversed_text = text[::-1]
print(reversed_text)  # Output: "olleh"
```


### 11. **sort()**
Sortuje listę w porządku rosnącym (lub malejącym, jeśli podasz argument `reverse=True`).

```python
my_list = [3, 1, 2]
my_list.sort()
print(my_list)  # [1, 2, 3]
```


#### 11A. `sorted()`
Zwraca posortowaną listę elementów.

```python
numbers = [3, 1, 4, 1, 5, 9]
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # Output: [1, 1, 3, 4, 5, 9]

# Przykład z ciągiem znaków
text = "python"
sorted_text = sorted(text)
print(sorted_text)  # Output: ['h', 'n', 'o', 'p', 't', 'y']
```

