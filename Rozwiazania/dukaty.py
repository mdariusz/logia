def dukaty(dzien):
    stan = 0
    for kolejny in range(1, dzien + 1):
        stan = stan + 1
        if kolejny % 5 == 0:
            stan = stan + 2
        if stan >= 50:
            stan = stan - (3 * stan) // 4
    return stan
