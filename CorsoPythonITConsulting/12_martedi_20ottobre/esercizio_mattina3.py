"""Consegna:
1.Utilizza np.linspace per creare un array di 50 numeri equidistanti tra 0 e 10.
2.Utilizza np.random.random per creare un array di 50 numeri casuali compresi tra 0
e 1.
3.Somma i due array elemento per elemento per ottenere un nuovo array.
4.Calcola la somma totale degli elementi del nuovo array.
5.Calcola la somma degli elementi del nuovo array che sono maggiori di 5.
6.Stampa gli array originali, il nuovo array risultante dalla somma e le somme
calcolate.
7.Salva i dati su un file TXT a ogni giro
8.Rendi ripetibile il processo complessivo
9.Chiedi se si vuole sovrascrivere il TXT o no.
Obiettivo:
Esercitarsi nell'utilizzo di linspace per generare sequenze di numeri, random per
creare array di numeri casuali, e sum per eseguire operazioni di somma sugli array,
incluso l'uso di condizioni per la somma parziale e gestire il salvataggio di file in
merito."""

#quindi posizione 0 su posizione 0, posizione 1 su posizione 1  per quanto riguarda la somma 


import numpy as np

array1 = np.linspace(0, 10, 50) #ragionare cosi: np.linspace(inizio, fine, numero_elementi) genera il numero di valori richiesto, distribuiti uniformemente tra gli estremi.

print(array1)

#array dei numeri casuali

array2 = np.random.random(50) #random.random ci fa direttamente l'array randomico dei 50 numeri compreso tra 0 e 1

print(array2)

array3 = array1 + array2 #con numpy posso direttamente sommare le pos gisute. quindi creo il terzo array e faccio sommare 1 e 2

print(array3)

somma_totale = np.sum(array3) #con sum e array 3, mi calcolo la somma totale velocemente

print(somma_totale)

#il punto 5 ovviamente mi ha fatto pemnsare subito ad un if, ma potrei farlo con maschera booleana
somma_maggiori_5 = np.sum(array3[array3 > 5])

print("n\print in fila") #punto 6, semplici print di tutto più ordinato

print("array1")
print(array1)

print("array2")
print(array2)

print("array somma")
print(array3)

print("array somma tot")
print(somma_totale)

print("array somma > 5")
print(somma_maggiori_5)


with open("risultati.txt", "w") as file:  #lo stavo provando così ma devo riguardarlo bene, provavo il path ma ancora non ci siamo
    file.write(str(array1) + "\n")
    file.write(str(array2) + "\n")
    file.write(str(array3) + "\n")
    file.write(str(somma_totale) + "\n")
    file.write(str(somma_maggiori_5) + "\n")
    
#manca l'extra ma me lo studio con calma