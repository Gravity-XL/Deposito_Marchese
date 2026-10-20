#LINSPACE

import numpy as np


arr = np.linspace(0, 1, 5)
print(arr)

#OUTPUT: [0.   0.25 0.5  0.75 1.  ]

#Mi ha stampato i range interni equidistanti da 0 a 1, utilizzimo per delle medie e creazione di dati artificiali
#EMULARE DATI

#RANDOM

random_arr = np.random.rand(3,3)
#matrice 3x3 con valori casuali uniformi tra 0 e 1
print(random_arr)

#posso trasformare quei valori con il x10 per spostare la virgola

print(random_arr)
print(random_arr * 10)


 #ROUND_PER FARE L'ARROTONDAMENTO CON IL NUMERO PIù VICINO
 
arr = np.array([1,2,3,4,5])

sum_value = np.sum(arr)
mean_value = np.mean(arr)
std_value = np.std(arr)

print("sum:", sum_value)
print("mean:", mean_value)
print("standard deviation:", std_value)

 
 
 
