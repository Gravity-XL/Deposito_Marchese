import numpy as np

arr = np.array([1,2,3,4,5])

#indexing
print(arr[0])  #output 1 

#slicing
print(arr[1:3]) #output [2,3] prende da un punto x a y (y escluso) e riporta tutti i valori che rientrano in quel campo, logica

#booleam indexing 
print(arr[arr > 2]) #output [3,4,5] tutti valori che superano questo elemento


#slicing su righe e colonne (negli esempi slide) 

#quando metto i 2 punti solo voglio la prima posizione di righe, quando metto lo spazio con la virgola, anche la seconda con le colonne (DA RIVEDERE SE HO SCRITTO CORETTAMENTE)


arr_2d = np.array([[1, 2, 3, 4],
                    [5, 6, 7, 8],
                    [9, 10, 11, 12]])


# Slicing sulle righe
print(arr_2d[1:3]) # Output: [[ 5 6 7 8]
# [ 9 10 11 12]]

# Slicing sulle colonne
print(arr_2d[:, 1:3]) # Output: [[ 2 3]
# [ 6 7]
# [10 11]]

# Slicing misto
print(arr_2d[1:3, 1:3]) # Output: [[ 6 7]
13. # [10 11]]

#start, stop, step(con salti di), se non mettiamo la fine la fine è inclusa

""" La sintassi base per lo slicing in NumPy è:
array[start:stop:step]
start: L'indice di inizio dello slicing (inclusivo). Se omesso, il valore
predefinito è 0.
stop: L'indice di fine dello slicing (esclusivo). Se omesso, il valore
predefinito è la dimensione dell'array.
step: Il passo tra un indice e l'altro. Se omesso, il valore predefinito è 1. """

print("________SLICING________")

# Slicing con passo
print(arr[1:8:2]) # Output: [1 3 5 7]

# Omettere start e stop
print(arr[:5]) # Output: [0 1 2 3 4]
print(arr[5:]) # Output: [5 6 7 8 9]

# Utilizzare indici negativi
print(arr[-5:]) # Output: [5 6 7 8 9]
print(arr[:-5]) # Output: [0 1 2 3 4]


