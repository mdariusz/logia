n = 5
karty = [1, 5, 3, 4, 5, 2, 3, 4, 2, 1]

pamiec = []   # lista zapamiętanych wartości
ruchy = 0

while karty:
    # odkrywamy ostatnią kartę
    a = karty.pop()
    
    if a in pamiec:
        # znam parę → usuwamy z pamiec
        pamiec.remove(a)
        # w każdym przypadku odsłonięto dwie karty → ruch += 1
        ruchy += 1
    else:
        # odkrywamy kolejną kartę
        b = karty.pop()
        ruchy += 1

        if a != b:
            # zapamiętujemy obie
            pamiec += [a, b]            
        # jeśli a == b, karty są już zdjęte, nic więcej nie trzeba robić

print(ruchy)
