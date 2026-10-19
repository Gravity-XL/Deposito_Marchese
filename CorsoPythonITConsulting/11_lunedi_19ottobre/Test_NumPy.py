import numpy as np

#creazione array unidimensionale

#lista = [1,2,3]
#arr = np.array(lista) 

#è come dire

arr = np.array([1,2,3,4,5])
print(arr)

#creazione di un array bidimensionale

arr2d = np.array([[1,2,3], [4,5,6]])
print(arr2d)

#dtype specifica il tipo di contenuti di dati nell'array (int fload bool etc)

arr = np.array([1, 2, 3], dtype='int32')
print(arr.dtype)

#shape serve a sapere la forma di un determinato elemento, dimensioni dell'array magari, uno ha 3 righe e uno 2, tra di loro non collaborano
#possiamo far lavorare tra loro elementi che hanno un grado di coerenza uguale
#due elementi con forme diverse non collaborano fra loro

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.shape) # Output: (2, 3) #due righe da 3 colonne, si parte sempre da 0, quindi riga 0 e 1 e colonna 0,1,2

#arange, crea un array direttamente in munpy senza passare da fuori, simile a range di python

arr = np.arange(10)
print(arr) # Output: [0 1 2 3 4 5 6 7 8 9] #si parte da 0 e fa 10 postazioni

#reshape,  cambia forma array senza modificare i dati, esempio della colonna, su comportamenti che hanno senso

arr = np.arange(6)
reshaped_arr = arr.reshape((2, 3))
print(reshaped_arr)
# Output: [[0 1 2] [3 4 5]]


