## str() - funkcje pozostałe

### 1. `capitalize()`
Funkcja ta zwraca nowy ciąg znaków, w którym pierwsza litera jest dużą literą, a pozostałe są małe.

**Przykład:**
```python
text = "hello world"
print(text.capitalize())  # Output: "Hello world"
```



### 2. `isalnum()`
Sprawdza, czy ciąg składa się tylko z liter i cyfr.

**Przykład:**
```python
text = "hello123"
print(text.isalnum())  # Output: True
```



### 3. `isalpha()`
Sprawdza, czy ciąg składa się tylko z liter.

**Przykład:**
```python
text = "hello"
print(text.isalpha())  # Output: True
```


## 4. `isdecimal()`
Sprawdza, czy ciąg składa się tylko z cyfr dziesiętnych (0-9). Nie akceptuje znaków ułamkowych, potęg, ani innych symboli liczbowych.

**Przykład:**
```python
text1 = "1234"
text2 = "1234.56"
print(text1.isdecimal())  # Output: True
print(text2.isdecimal())  # Output: False
```

## 6. `isnumeric()`
Sprawdza, czy ciąg składa się z cyfr lub innych znaków liczbowych, takich jak liczby ułamkowe, potęgi czy cyfry w innych systemach liczbowych.

**Przykład:**
```python
text1 = "٢٣٤٥"  # Cyfry arabskie
text2 = "⅓"    # Ułamek
print(text1.isnumeric())  # Output: True
print(text2.isnumeric())  # Output: True
```



### 5. `isdigit()`
Sprawdza, czy ciąg składa się tylko z cyfr.

**Przykład:**
```python
text = "1234"
print(text.isdigit())  # Output: True
```



### 6. `isnumeric()`
Funkcja **`isnumeric()`** sprawdza, czy wszystkie znaki w ciągu są cyframi lub innymi znakami liczbowymi. Obejmuje zwykłe cyfry (0-9), cyfry w innych systemach liczbowych, potęgi, ułamki, itp.

### Przykład:
```python
# Przykłady z różnymi typami znaków liczbowych
examples = [
    "1234",    # Zwykłe cyfry
    "٥٦٧٨",    # Cyfry arabskie
    "⅔",       # Ułamek
    "²³",      # Potęgi
    "123.45",  # Zawiera kropkę, nie jest numeric
    "Ⅷ",       # Cyfra rzymska
    "一二三四"   # Cyfry chińskie
]

for text in examples:
    print(f"{text}: {text.isnumeric()}")
```

### Wynik:
```
1234: True        # Zwykłe cyfry
٥٦٧٨: True        # Cyfry arabskie
⅔: True           # Ułamek
²³: True          # Potęgi
123.45: False     # Zawiera kropkę
Ⅷ: False          # Cyfra rzymska (nie jest numeric)
一二三四: True     # Cyfry chińskie
```

**Podsumowanie**: `isnumeric()` zwraca `True` dla ciągów składających się z cyfr dziesiętnych oraz innych znaków liczbowych, ale nie dla ciągów zawierających znaki, które nie są wyłącznie liczbami, jak np. kropka dziesiętna czy cyfry rzymskie.



### 7. `islower()`
Sprawdza, czy wszystkie litery w ciągu są małe.

**Przykład:**
```python
text = "hello"
print(text.islower())  # Output: True
```



### 8. `isupper()`
Sprawdza, czy wszystkie litery w ciągu są wielkie.

**Przykład:**
```python
text = "HELLO"
print(text.isupper())  # Output: True
```



### 9. `endswith()`
Sprawdza, czy ciąg kończy się określonym sufiksem.

**Przykład:**
```python
text = "hello world"
print(text.endswith("world"))  # Output: True
```



### 10. `startswith()`
Sprawdza, czy ciąg zaczyna się od określonego prefiksu.

**Przykład:**
```python
text = "hello world"
print(text.startswith("hello"))  # Output: True
```



### 11. `swapcase()`
Zmienia wielkość liter: małe na wielkie i odwrotnie.

**Przykład:**
```python
text = "Hello World"
print(text.swapcase())  # Output: "hELLO wORLD"
```



### 12. `zfill()`
Wypełnia ciąg znakami '0' z lewej strony, aby uzyskać określoną długość.

**Przykład:**
```python
text = "42"
print(text.zfill(5))  # Output: "00042"
```



### 13. `partition()`
Dzieli ciąg na 3 części: przed pierwszym wystąpieniem separatora, separator i po nim.

**Przykład:**
```python
text = "hello,world"
print(text.partition(','))  # Output: ('hello', ',', 'world')
```


## Pozostałe

| **Funkcja**        | **Opis**                                                                 |
|--------------------|---------------------------------------------------------------------------|
| `casefold()`       | Zamienia wszystkie litery w ciągu na małe i wykonuje normalizację, umożliwiając porównywanie ciągów w sposób niezależny od wielkości liter. |
| `center()`         | Wyrównuje ciąg do środka, dodając określoną liczbę znaków z lewej i prawej strony. |
| `expandtabs()`     | Zastępuje znaki tabulacji odpowiednią liczbą spacji.                      |
| `format_map()`     | Formatuje ciąg z użyciem słownika, podobnie jak `format()`, ale z różnymi opcjami dostosowywania. |
| `isascii()`        | Sprawdza, czy wszystkie znaki w ciągu są znakami ASCII.                   |
| `isidentifier()`   | Sprawdza, czy ciąg jest prawidłowym identyfikatorem (np. nazwą zmiennej w Pythonie). |
| `isprintable()`    | Sprawdza, czy ciąg zawiera tylko znaki, które można wyświetlić.           |
| `isspace()`        | Sprawdza, czy ciąg składa się tylko z białych znaków (spacje, tabulatory, itp.). |
| `istitle()`        | Sprawdza, czy każdy wyraz w ciągu zaczyna się wielką literą, a pozostałe litery są małe. |
| `ljust()`          | Wyrównuje ciąg do lewej strony, dodając określoną liczbę znaków z prawej strony. |
| `lstrip()`         | Usuwa białe znaki (lub inne podane znaki) z lewej strony ciągu.           |
| `maketrans()`      | Tworzy tabelę tłumaczeń do użycia w funkcji `translate()`.                 |
| `removeprefix()`   | Usuwa określony prefiks z ciągu, jeśli występuje.                         |
| `removesuffix()`   | Usuwa określony sufiks z ciągu, jeśli występuje.                         |
| `rfind()`          | Zwraca indeks ostatniego wystąpienia podciągu w ciągu, lub -1, jeśli nie znaleziono. |
| `rindex()`         | Zwraca indeks ostatniego wystąpienia podciągu w ciągu, generując błąd, jeśli nie znaleziono. |
| `rjust()`          | Wyrównuje ciąg do prawej strony, dodając określoną liczbę znaków z lewej strony. |
| `rpartition()`     | Dzieli ciąg na trzy części, szukając ostatniego wystąpienia określonego podciągu. |
| `rsplit()`         | Dzieli ciąg na listę podciągów, zaczynając od prawej strony.               |
| `rstrip()`         | Usuwa białe znaki (lub inne podane znaki) z prawej strony ciągu.           |
| `title()`          | Zamienia pierwszą literę każdego wyrazu na wielką literę, a pozostałe na małe. |
| `translate()`      | Używa tabeli tłumaczeń (z `maketrans()`), by zamienić znaki w ciągu.       |


