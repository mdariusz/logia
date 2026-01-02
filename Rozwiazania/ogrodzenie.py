n = int(input())
lista = input().split()

p = []
suma = 0

for i in range(n):
    p.append(int(lista[i]))
    suma += int(lista[i])

maksymalna = 0

for i in range(n - 2):
    for j in range(i + 2, n):
        if not (i == 0 and j == n - 1):
            if p[i] + p[j] > maksymalna:
                maksymalna = p[i] + p[j]

print(suma - maksymalna)
