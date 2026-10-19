""" Es1: ndarray, dtype, shape, arange
Crea due array NumPy utilizzando arange e
verifica il tipo di dato (dtype) e la forma
(shape) dell'array, con dimensioni differenti.
Esercizio:
1. Utilizza la funzione np.arange per creare
un array di numeri interi da 10 a 49.
2. Verifica il tipo di dato dell'array e
stampa il risultato.
3. Cambia il tipo di dato dell'array in
float64 e verifica di nuovo il tipo di
dato.
4. Stampa la forma dell'array. """

import numpy as np

# Creazione di un array
arr = np.arange(10, 50)
print(arr)

print(arr.dtype)

arr = np.array(arr, dtype=np.float64) #a questo punto se non posso usare astype lo riassegno come float
print(arr.dtype) #sopra mi stampa l'int ed ora mi stampera float64

print(arr.shape) 
