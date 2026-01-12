def sito(N):
    pierwsze = []
    for i in range(N + 1):
        if i % 2 == 1:
            pierwsze.append(True)
        else:
            pierwsze.append(False)

    pierwsze[1] = False
    pierwsze[2] = True
    
    for i, liczba in enumerate(pierwsze):
        print(i, liczba, end= " |")
    
    for dzielnik in range(N+1):
        if pierwsze[dzielnik]:
            for i in range(dzielnik * dzielnik, N+1, dzielnik
            pierwsze[i] = False
    
        
	# Wyswietlenie
    print("\n")		
    print("-" * 30)
    for i, liczba in range(N+1)
        if pierwsze[i]:
			print(liczba)



sito(28)
