### str() - funkcje podstawowe

#### 1. `count()`
Zlicza wystąpienia podłańcucha w ciągu.

```python
text = "hello world"
print(text.count('o'))  # Output: 2
```

#### 2. `format()`
Formatuje ciąg znaków, wstawiając wartości.

```python
text = "Hello, {}!"
print(text.format("Alice"))  # Output: Hello, Alice!
```

#### 3. `index()`
Zwraca indeks pierwszego wystąpienia podłańcucha. Rzuca wyjątek, jeśli podłańcuch nie zostanie znaleziony.

```python
text = "hello world"
print(text.index('o'))  # Output: 4
```

#### 4. `find()`
Zwraca indeks pierwszego wystąpienia podłańcucha. Zwraca -1, jeśli podłańcuch nie zostanie znaleziony.

```python
text = "hello world"
print(text.find('o'))  # Output: 4
```

#### 5. `join()`
Łączy elementy iterowalne, używając ciągu jako separatora.

```python
words = ['hello', 'world']
print(' '.join(words))  # Output: "hello world"
```

#### 6. `strip()`
Usuwa białe znaki z początku i końca ciągu.

#### 7. `replace()`
Zamienia wszystkie wystąpienia podłańcucha na inny podłańcuch.

```python
text = "hello world"
print(text.replace('world', 'Python'))  # Output: "hello Python"
```

#### 8. `lower()`
Konwertuje wszystkie znaki w ciągu na małe litery.

```python
text = "Hello World"
print(text.lower())  # Output: "hello world"
```

#### 9. `upper()`
Konwertuje wszystkie znaki w ciągu na wielkie litery.

```python
text = "hello world"
print(text.upper())  # Output: "HELLO WORLD"
```

#### 10. `split()
Rozdziela ciąg znaków na listę, używając separatora (domyślnie spacji).

```python
text = "hello world"
words = text.split()
print(words)  # Output: ["hello", "world"]

# Przykład z niestandardowym separatorem
text_with_commas = "apple,banana,cherry"
fruits = text_with_commas.split(',')
print(fruits)  # Output: ["apple", "banana", "cherry"]
```

## Przykłady z `in` i prostymi `if` dla listy i stringa

### 1. **Dla listy**:

Operator `in` sprawdza, czy element znajduje się w liście.

```python
# Lista liczb
my_list = [1, 2, 3, 4, 5]

# Sprawdzanie, czy element 3 znajduje się w liście
if 3 in my_list:
    print("3 is in the list.")  # Output: 3 is in the list.
else:
    print("3 is not in the list.")

# Sprawdzanie, czy element 6 znajduje się w liście
if 6 in my_list:
    print("6 is in the list.")
else:
    print("6 is not in the list.")  # Output: 6 is not in the list.
```

### 2. **Dla stringa**:

Operator `in` sprawdza, czy substring (ciąg znaków) znajduje się w stringu.

```python
# String
my_string = "Hello, World!"

# Sprawdzanie, czy substring "Hello" znajduje się w stringu
if "Hello" in my_string:
    print("Found 'Hello' in the string.")  # Output: Found 'Hello' in the string.
else:
    print("'Hello' is not in the string.")

# Sprawdzanie, czy substring "world" (z małej litery) znajduje się w stringu
if "world" in my_string:
    print("Found 'world' in the string.")
else:
    print("'world' is not in the string.")  # Output: 'world' is not in the string. (case-sensitive)
```

### 3. **Dla listy stringów**:

Sprawdzanie, czy dany string znajduje się w liście stringów.

```python
# Lista stringów
my_list = ["apple", "banana", "cherry"]

# Sprawdzanie, czy element "banana" znajduje się w liście
if "banana" in my_list:
    print("Found 'banana' in the list.")  # Output: Found 'banana' in the list.
else:
    print("'banana' is not in the list.")

# Sprawdzanie, czy element "grape" znajduje się w liście
if "grape" in my_list:
    print("Found 'grape' in the list.")
else:
    print("'grape' is not in the list.")  # Output: 'grape' is not in the list.
```

