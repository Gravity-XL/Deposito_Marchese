

"""Esercizio 1: Somma e Media di Elementi
Creare un array NumPy di 15 elementi contenente numeri casuali compresi tra 1 e 100.
Calcolare e stampare la somma di tutti gli elementi dell'array.
Calcolare e stampare la media di tutti gli elementi dell'array.
Esercizio 2: Manipolazione di Array Multidimensionali
Creare una matrice 5x5 contenente numeri interi sequenziali da 1 a 25.
Estrarre e stampare la seconda colonna della matrice.
Estrarre e stampare la terza riga della matrice.
Calcolare e stampare la somma degli elementi della diagonale principale della matrice.
Esercizio 3: Operazioni con Fancy Indexing
Creare un array NumPy di forma (4, 4) contenente numeri casuali interi tra 10 e 50.
Utilizzare fancy indexing per selezionare e stampare gli elementi agli indici (0, 1), (1, 3), (2, 2) e
(3, 0).
Utilizzare fancy indexing per selezionare e stampare tutte le righe dispari dell'array (considerando la
numerazione delle righe che parte da 0).
Modificare gli elementi selezionati nel primo punto dell'esercizio aggiungendo 10 al loro valore."""

# extra ripetibile, e su file di testo i risultati


import numpy as np

#es1


casuali = np.random.randint(1,101, size=15) 
print("Questi sono i numeri casuali:", casuali)


np.sum(casuali)
print("Somma di tutti i numeri casuali: ", np.sum(casuali))

np.mean(casuali)
print("Media di tutti i numeri casuali: ", np.mean(casuali))


#es2

array1 = np.arange( 1, 26)
print("Creo la matrice di numeri da 1 a 25: ", array1)

array_2d = array1.reshape(5,5)
print("Creo la matrice 5x5: ", array_2d)

#selezionare tutte le righe (quindi [:,1], da ricordare, altrimenti come faccio a riempire le colone???)
print("Stampa della seconda colonna della matrice: ", array_2d[:, 1])

#selezionare tutte le righe (quindi [2, :], quindi l'inverso di sopra) fatta in un secondo
print("Stampa della terza riga della matrice: ", array_2d[2, :])


#IMPORTANTE!!! Lo stesso dubbio dell'altra volta su cose diverse
#una fotla che ho estratto ciò che mi interessa (DIAGONALE) in questo caso
#per fare la somma, senza troppi giri, ripeto sempre np.sum avanti a quello che mi ero estratto
#un attimo prima, se devo solo printarla, (verificare che il return funziona, a volte potrebbe non funzionare)
print("Elementi della diagonale principale: ", np.diag(array_2d))
print("Somma della diagonale principale: ", np.sum(np.diag(array_2d)))

#es 3 operazioni con Fancy Indexing

#DA RIVEDERE !!!!! l'ho ricercata in rete, nel caso chiedere a mirko se ci sono dubbi
#arra3, np.random.randint (e scrivo direttamente i casuali che mi interessano, e la grandezza della matrice che voglio)
array3 = np.random.randint(10, 51, size = (4, 4))
print("Matrice 4x4 con numeri casuali:", array3)

#faccioestrarre un singolo elemento usando indice della riga e indice della colonna.
print(array3[0, 1])
print(array3[1, 3])
print(array3[2, 2])
print(array3[3, 0])


# RIGa, la prima dice che parte da 0, quindi 0-1DISPARI-2-3dISPARI (2 step una volta impostata la prima lal fine

print("Righe dispari:", array3[1::2])

array3[[0, 1, 2, 3], [1, 3, 2, 0]] += 10

print("broadcasting: ", array3)





