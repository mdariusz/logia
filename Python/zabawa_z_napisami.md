

```markdown
 0   1   2   3   4   5   6
 g   r   a   f   i   k   a
-7  -6  -5  -4  -3  -2  -1
```
```python
for i in range(1,len(s)+1):
    print(-i," ",s[-i])
print()
```

```python
start = 0
end = 5
step = 3
wyraz = "Wypisanie"
print("Długość: ",len(wyraz))
print("Start: {}. End: {}. Step: {}".format(start,end,step))
print("Kawalątek",wyraz[start:end:step])
```

```python
#wypisanie fragmentu bez 4 pierwszych znaków
print(s[4:])
print()
#wypisanie fragmentu - dwóch pierwszych znaków
print(s[:2])
print()
#wypisanie ciągu znaków od trzeciego do szóstego
print(s[2:6])
print()
#wypisanie pięciu ostatnich znaków napisu
print(s[-5:])
print()
```