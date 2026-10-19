"""Esercizio 2 Slicing e F.Indexing
Consegna:
1. Crea una matrice NumPy 2D di dimensioni 6x6 contenente
numeri interi casuali compresi tra 1 e 100.
2. Estrai la sotto-matrice centrale 4x4 dalla matrice
originale.
3. Inverti le righe della matrice estratta (cioè, la prima riga
diventa l'ultima, la seconda diventa la penultima, e così
via).
4. Estrai la diagonale principale della matrice invertita e
crea un array 1D contenente questi elementi.
5. Sostituisci tutti gli elementi della matrice invertita che
sono multipli di 3 con il valore -1.
6. Stampa la matrice originale, la sotto-matrice centrale
estratta, la matrice invertita, la diagonale principale e la
matrice invertita modificata."""

import numpy as np

matrice_originale = np.random.randint(1, 101, size=[6, 6]) #creo la prima matrice con i numeri random da 1 a 100 grandezza 6,6
print(matrice_originale)

sotto_matrice = matrice_originale[1:5, 1:5] #giustamente per prendermi i centrali faccio fuori gli estremi (sia ai lati che sopra e sotto, QUINDI 4X4), quindi levo posizione 0 e 5
print(sotto_matrice)

matrice_invertita = sotto_matrice[::-1, :] #in questo modo invertiamo le righe della matrice, la prima diventa l'ultima, la seconda pen ecc
print(matrice_invertita)

diagonale = np.diag(matrice_invertita) #questo metodo np.diag è un metodo che ti prende la diagonale automaticamente
print(diagonale) 

#ATTENZIONE, mettiamo volessi prendere la diagonale opposta? ho trovato questo metodo che permette di fare la cosa opporta
#o volendo potrei prendere la diagonale come ho fatto sopra,diagonale_secondaria = np.diag(matrice_invertita[:, ::-1]) e aggiungerci il -1 finale, il risultato sarebbe lo stesso per prendere l'altro angolo
### diagonale_secondaria = np.diag(np.fliplr(matrice_invertita))

## POTEVO FARLO CON INDICIZZAZIONE BOOLEANA
# 
# matrice_invertita[matrice_invertita % 3 == 0] = -1 #con
#print(matrice_invertita)

#IN QUESTO CASO PER ALLENAMENTO FACCIAMOLO CON IL FOR PER MUOVERCI MEGLIO ALL'INTERNO DELLE MATRICI

# Spacchettiamo la tupla direttamente in due variabili: righe e colonne
righe, colonne = matrice_invertita.shape 

# Ora usiamo queste variabili nel range del ciclo for
for r in range(righe):
    for c in range(colonne):
        if matrice_invertita[r, c] % 3 == 0:
            matrice_invertita[r, c] = -1

print("5. Matrice modificata con il ciclo FOR:")
print(matrice_invertita)

print("______TUTTE LE STAMPE______")

print("Matrice originale:") #Original
print(matrice_originale)

print("Sotto-matrice centrale:") #centrale
print(sotto_matrice)

print("Matrice invertita:") #invertita
print(matrice_invertita)

print("Diagonale principale:") #diagonale da i alto a sinistra, in basso a destra
print(diagonale)



