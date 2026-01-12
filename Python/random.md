## Python `random` — przykładowy kod


```python
import random

# losowa liczba float z [0.0, 1.0)
x = random.random()

# losowa liczba całkowita z przedziału [1, 10]
a = random.randint(1, 10)

# losowa liczba z zakresu range(0, 20, 2)
b = random.randrange(0, 20, 2)

# losowy element sekwencji
c = random.choice(['a', 'b', 'c', 'd'])

# 3 unikalne elementy z listy
d = random.sample([1, 2, 3, 4, 5], 3)

# tasowanie listy (in-place)
lst = [1, 2, 3, 4]
random.shuffle(lst)
