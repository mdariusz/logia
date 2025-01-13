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
