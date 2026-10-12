 #__________METODO STATICO_____
    
class Calcolatrice:
    
    @staticmethod
    def somma(a, b):
        return a + b 
    
#Uso del metodo statico senza creare un'istanza
risultato = Calcolatrice.somma(5,3)

print(risultato)
#Output: 8

class Contatore:
    numero_istanze = 0 #attributo di classe
    
    def __init__(self):
        Contatore.numero_istanze += 1
        
    @classmethod
    def mostra_numero_istanze(cls):
        print("Sono state create", cls.numero_istanze, "istanze.")
        
#creazione di alcune istanze
c1 = Contatore()
c2 = Contatore()

Contatore.mostra_numero_istanze()
#output: Sono state create 2 istanze.    
    
    