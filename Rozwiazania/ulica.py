def maksos(ulica):
    lista_osiedli = []
    osiedle = [ulica[0]]
    for i in range(1, len(ulica) - 1):
        if (ulica[i] - ulica[i - 1]) <= 3:
            osiedle.append(ulica[i])
        else:
            lista_osiedli.append(osiedle)
            osiedle = [ulica[i]]
    lista_osiedli.append(osiedle)
    print(lista_osiedli)
    pierwsze_osiedle = lista_osiedli[0]
    if (1 in pierwsze_osiedle) or (2 in pierwsze_osiedle) or (3 in pierwsze_osiedle):
        lista_osiedli[0].append(ulica[-1])
    else:
        lista_osiedli[-1].append(ulica[-1])




maksos([1,4,7,13,14,15,20])