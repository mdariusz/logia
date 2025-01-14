# Zadanie 1/2023 - Szyfr trójkątny

from turtle import *

# 0, 1 , 2

# lista_cyfr = ["0000", "0001", ...]
def szyfruj(cyfra):
    dw = ''
    for i in range(4):
        dw = str(cyfra % 2) + dw
        cyfra = cyfra // 2
    return dw
    #0: 9 % 2 = 1     9 // 2 = 4
    #1: 4 % 2 = 0     4 // 2 = 2
    #2: 2 % 2 = 0     2 // 2 = 1
    #3  1 % 2 = 1     1 // 2 = 0

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

# print(szyfruj(0))
tracer(0)
trojkat(40, "1")
update()
mainloop()

#
#
# tracer(0)
# pasek(1234567, 40)
# # trojkat(30, "red")
# #rysuj_jedna_cyfra(40, 8)
# update()
# mainloop()