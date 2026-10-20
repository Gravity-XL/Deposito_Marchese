"""Crea uno script Python che esegua i seguenti passaggi:
1. Crea un array NumPy (ndarray) utilizzando np.arange con valori da 0 a
49. più altre 50 posizioni casuali tra 49 e 101.
Stampa l’array, il suo dtype e la sua shape.
2. Modifica il tipo di dato (dtype) dell’array in float64.
Verifica e stampa di nuovo dtype e shape.
3. Utilizza lo slicing per ottenere:
i primi 10 elementi
gli ultimi 7 elementi
gli elementi dall’indice 5 all’indice 20 escluso
ogni quarto elemento dell'array
4. Modifica tramite slicing gli elementi dall’indice 10 a 15 (escluso)
assegnando loro il valore 999.
5. Utilizza la fancy indexing per selezionare:
gli elementi in posizione [0, 3, 7, 12, 25, 33, 48]
tutti gli elementi pari dell’array utilizzando una maschera booleana
tutti gli elementi maggiori della media dell'array
6. Stampa:
l’array originale dopo tutte le modifiche
tutti i sotto-array ottenuti tramite slicing e fancy indexin"""


import numpy as np

numeri = np.arange(50) #primo array

casuali = np.random.randint(49,101, size=50) #secondo array

numeri = np.concatenate((numeri,casuali)) #concateniamo i 2 array e li riassegnamo a numeri

print(numeri)
print(numeri.dtype)
print(numeri.shape)

#DA RIVEDERE ASTYPE O SE PUO' ANDARE COSI
numeri = np.array(numeri, dtype=np.float64) #cambiamo da int a float, ma dovevo farlo con astype forse
print(numeri.dtype)
print(numeri.shape)

#slicing primi 10 num, ricorda array [inizio : fine], usiamo sempre - nell'inizio per prendere gli ultimi


numeri[:10]
print(numeri[:10])  

numeri[:-7]
print(numeri[-7:])

numeri[5:20] #da chiedere a mirko, ma a sto punto posso anche solo printare senza questo?
print(numeri[5:20]) 

#OGNI QUARTO ELEMENTO DELL'ARRAY IDENTICO ALLA SCORSA VOLTA, DA RICORDARE
#array[inizio:fine:passo] ragionare così 

numeri[::4]
print(numeri[::4])

#999, da 10 a 15

numeri[10:15] = 999 #solito discorso INIZIO-FINE, "array[inizio:fine] = valore che voglio inserire" modifica tutti gli elementi compresi nell'intervallo, senza includere l'indice finale.
print(numeri)

# Elementi in posizioni specifiche, mi sono scritto esattamente le posizioni e le ho printate, penso che intendeva questo, selezionare i numeri ma non modificarli creando un nuovo array
print(numeri[[0, 3, 7, 12, 25, 33, 48]])

# Tutti gli elementi pari, come ieri maschera booleana, classico %2 ==0 per i pari
print(numeri[numeri % 2 == 0])

#MEDIA NUMERI, NP.MEAN DA RICORDARE
# Tutti gli elementi maggiori della media, questo l'ho cercato, np.mean 
print(numeri[numeri > np.mean(numeri)])

#stampo tutto
print("\n___stampiamo tutto ciò che abbiamo fatto in ordine___\n")

# Array originale dopo tutte le modifiche fatte
print("\nArray originale modificato:\n")
print(numeri)

# Slicing: primi 10 elementi dell'array
print("\nPrimi 10 elementi:\n")
print(numeri[:10])

# Slicing: ogni quarto elemento
print("\nOgni quarto elemento:\n")
print(numeri[::4])

# Fancy indexing: posizioni specifiche
print("\nElementi in posizioni specifiche:\n")
print(numeri[[0, 3, 7, 12, 25, 33, 48]])

# Maschera booleana: elementi pari
print("\nElementi pari:\n")
print(numeri[numeri % 2 == 0])

# Maschera booleana: elementi maggiori della media, riguardare bene magari
print("\nElementi maggiori della media:\n")
print(numeri[numeri > np.mean(numeri)])

