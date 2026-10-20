"""crea un array utilizzando linespace, cambia la sua forma con reshape, venera un array casuale e calcola la somma degli elementi

esercizio:

crea un array di 12 numeri equidistanti tra 0 e 1 usando linespace.
cambia la forma dell'array a una matrice 3x4
genera una matrice 3x4 di numeri casuali tra 0 e 1
calcola e stampa la somma degli elementi di entrambe le matrici"""


import numpy as np

numeri = np.linspace(0, 1, 12) #ragionare cosi: np.linspace(inizio, fine, numero_elementi) genera il numero di valori richiesto, distribuiti uniformemente tra gli estremi.

print(numeri)

#reshape 3,4 per la forma

matrice = numeri.reshape(3, 4)

print(matrice)

#i casuali, solito con i valori alla fine 3X4

casuali = np.random.random((3, 4))

print(casuali)


#convertiamole in numeri interi con il x10 che mi sono segnato prima in test prove

print(casuali * 10)

#per farlo più carino posso provare quel metodo chiesto a mirco, l'arrotondamento
#mi riporto il *10 giustamente per averli anche già moltiplicati in interi

print(np.round (casuali*10))

#astype l'ho usato direttamente nel print cosi volevo usare sia la conversione che l'arrotondare da un *10


print("\n\n========== STAMPA FINALE PULITA ==========\n")

print("MATRICE INIZIALE:")
print(matrice)

print("\nMATRICE CASUALE:")
print(casuali)

print("\nMATRICE CASUALE MOLTIPLICATA PER 10:")
print(casuali * 10)

print("\nMATRICE MOLTIPLICATA PER 10 E ARROTONDATA:")
print(np.round(casuali * 10))

print("\nMATRICE MOLTIPLICATA PER 10, ARROTONDATA E CONVERTITA IN INTERI:")
print(np.round(casuali * 10).astype(int))

print("\n==========================================\n")


