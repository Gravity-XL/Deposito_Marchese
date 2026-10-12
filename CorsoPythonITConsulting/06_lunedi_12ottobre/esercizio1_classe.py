
    
"""class Calcolatrice:
    
    @staticmethod
    def somma(a, b):
        return a + b 
    
#Uso del metodo statico senza creare un'istanza
risultato = Calcolatrice.somma(5,3) 

print(risultato)
#Output: 8   """

#esercizio 1

class Punto:

   def __init__(self, x = 0, y =0):
    self.x = x
    self.y = y

    def muovi(self, dx:int, dy:int):
     self.x = dx
     self.y = dy   
    
    def distanza_da_origine(self):
        return (self.x-0, self.x-0) # punto di partenza
    

    
#da completare gli int ec

# INIZIO UN ESERCIZIO SULLE CLASSI DEFINENDO LA CLASSE CHE MI SERVE

#SICURAMENTE SERVIRà UN COSTRUTTORE e devo assegnarle

class punto:

    def __init__(self,x,y):
        self.x = x
        self.y = y 
    
    #drrviva muovi punti
    def muovi_punti(self,dx,dy):
        self.x=dx
        self.x=dy
        
    def distanza_origine(self):
        return self.x, self.y
    
    def __str__(self):
        return "ciao sono un str"
     
x = input()   
y = input()

punto mio = punto(x,y)

print(punto_mio) #non stampa l'interno dei due punto, ma ti stampa la posizione precisa nella macchina
