import matplotlib.pyplot as plt

#DA UTILIZZARE PER UN UTILITY "VISUALIZZAZIONE", le spiegazioni sono in linea di
#massima nell'esercizio successivo, controllare i commenti!


#GRAFICO LINEARE
"""

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.figure()
plt.plot(x, y)
plt.title('Grafico a Linee')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.show()

"""

#GRAFICO A BARRE

"""categories = ['A', 'B', 'C', 'D', 'E']
values = [3, 7, 2, 5, 8]

plt.figure()
plt.bar(categories, values)
plt.title('Grafico a Barre')
plt.xlabel('Categorie')
plt.ylabel('Valori')
plt.show() 

"""

#ISTOGRAMMA

"""
import numpy as np
import matplotlib.pyplot as plt

data = np.random.randn(1000)

plt.figure()
plt.hist(data, bins=30)
plt.title('Istogramma')
plt.xlabel('Valori')
plt.ylabel('Frequenza')
plt.show()

"""

#SCATTER PLOT

"""

import numpy as np
import matplotlib.pyplot as plt

x = np.random.rand(50)
y = np.random.rand(50)

plt.figure()
plt.scatter(x, y)
plt.title('Scatter Plot')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.show()

"""