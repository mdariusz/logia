## Zadanie 1/2020_e2 - Kwadratowy szyfr

from turtle import *

def alfabet():
    tab = []
    for i in range(26):
        tab += chr(i + 97)
    return tab

def kwadrat(bok):
    for i in range(4):
        fd(bok); rt(90)

def kwadrat_cz(bok):
    fillcolor("red")
    begin_fill()
    kwadrat(bok)
    end_fill()

def rysuj(litera, bok):
    tab = alfabet()
    for i in range(26):
        if litera != tab[i]:
            kwadrat(bok)
        else:
            kwadrat_cz(bok)
        fd(bok)
        if i == 12:
            rt(90); fd(2 * bok); rt(90)

def koduj(napis):
    bok = 760 / (2 * len(napis))
    pu()
    bk(760 / 2)
    lt(90)
    bk(13 * bok / 2)
    pd()
    for zn in napis:
        rysuj(zn, bok)
        lt(180)



tracer(0)
koduj("napisik")
update()
done()

