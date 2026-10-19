""" Esercizio Slicing e F.Indexing
Esercizio su NumPy Slicing
Consegna:
1. Crea un array NumPy 1D di 20 numeri interi casuali compresi
tra 10 e 50.
2. Utilizza lo slicing per estrarre i primi 10 elementi
dell'array.
3. Utilizza lo slicing per estrarre gli ultimi 5 elementi
dell'array.
4. Utilizza lo slicing per estrarre gli elementi dall'indice 5
all'indice 15 (escluso).
5. Utilizza lo slicing per estrarre ogni terzo elemento
dell'array.
6. Modifica, tramite slicing, gli elementi dall'indice 5
all'indice 10 (escluso) assegnando loro il valore 99.
7. Stampa l'array originale e tutti i sottoarray ottenuti tramite
slicing.
Obiettivo:
Esercitarsi nell'utilizzo dello slicing di NumPy per estrarre e
modificare sottoarray specifici da un array più grande. """

import numpy as np

arr = np.random.randint(10, 51, size=20)  #con random random int possiamo fare i casuali 10-51 con size = 20
print(arr)
#  La sintassi base per lo slicing in NumPy è: (punto 2 dell'esercizio)
#         array[start:stop:step] 

print(arr[:10]) #i primi 10 numeri

print(arr[-5:]) #gli ultimi 5 (prende gli ultimi 5 a partire da in fondo)

print(arr[5:15]) #da posizione INDICE 5 , quindi dal sesto numero, alla posizione indice 15(esclusa)

print(arr[2::3]) #con passo, ogni terzo elemento, ho messo l'inizio a 2 così i primi 2 elementi li salta, e stampa dal terzo e va avanti così

#print("_____new array_____ e lo modifichiamo a con il numero 99 dove richiesto")

#arr = np.random.randint(10, 51, size=20) #printo il vecchio array
#print(arr) i commenti li ho messi giusto se voelvamo cambiare numeri

arr[5:10] = 99 #printo il nuovo array assegnando 99 a posizioni 5:10 escludendo il 10
print(arr)

#i commenti sopra questo ultimo arrai li ho messi giusto se voelvamo cambiare nu

