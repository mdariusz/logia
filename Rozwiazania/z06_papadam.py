# wiadomosc = input()
wiadomosc = "ppaaapapdaaamppappaaadapmpapaapadpamaa" #3
#            p a  papda  mp a pa  da mpapa   d am
#            |           ||          ||         |
#            |     1     ||    2     ||    3    |


# wiadomosc = "ppapadaaaamaaapaappaddmppaapadaaaamppaa" #2
# wiadomosc = "papadampapadampapadampapadam" #4

ile_szukany = 0
indeks_szukany = 0 # kolejna litera `szukany='papadam'
szukany = 'papadam'
dlugosc_wiadomosc = len(wiadomosc)
dlugosc_szukany = len(szukany) # 7


for i in range(dlugosc_wiadomosc):
    if wiadomosc[i] == szukany[indeks_szukany]:
        indeks_szukany += 1
        if indeks_szukany == dlugosc_szukany: # [] == 7
            indeks_szukany = 0
            ile_szukany += 1

print(ile_szukany)
