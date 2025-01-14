# Zadanie 1/2023 - Szyfr trójkątny

from turtle import *

def szyfruj(cyfra):
    dw = ''
    for i in range(4):
        dw = str(cyfra % 2) + dw
        cyfra = cyfra // 2
    return dw

def rysuj_jedna_cyfra(bok, cyfra):
    cyfra_bin = szyfruj(cyfra)
    trojkat(bok, cyfra_bin[0])
    fd(bok)
    lt(60)
    trojkat(bok, cyfra_bin[1])
    rt(60)
    trojkat(bok, cyfra_bin[2])
    fd(bok)
    lt(60)
    trojkat(bok, cyfra_bin[3])
    rt(60)

def trojkat(bok, cyfra_bin):
    if cyfra_bin == '0':
        fillcolor('white')
    else:
        fillcolor('green')
    begin_fill()
    for i in range(3):
        fd(bok)
        lt(120)
    end_fill()

def pasek(liczba, bok):
    liczba_str = str(liczba)
    przesuniecie = bok * len(liczba_str) + bok / 4
    pu()
    bk(przesuniecie)
    pd()
    for cyfra_str in liczba_str:
        rysuj_jedna_cyfra(bok, int(cyfra_str))

print(szyfruj(9))


tracer(0)
pasek(1234567, 40)
# trojkat(30, "red")
#rysuj_jedna_cyfra(40, 8)
update()
mainloop()