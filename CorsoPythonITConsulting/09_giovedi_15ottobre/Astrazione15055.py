

#from abc import ABC, abstractmethod  #importiamo una classe e un decoratore #dalla libreria abc importami abstract method

#non può diventare un oggetto, il decoratore ti permette di lasciare metodi vuoti e costringere i figli a sovrastiverti

#il figlio quindi prenderà il metodo , lo riscriverà, e a quel punto potrà diventare un oggetto, 

#se non lo sovrascriviamo e creiamo un oggetto di una classe astratta, python non può sapere fino alla fine che non può crearlo, 
#ci darà errore solo quando lo lancerà

#puo avere variabili, ha in più che 

from abc import ABC, abstractmethod

class Pippo_Astratto(ABC): #dalla libreria abc importami abstract method
    
    @abstractmethod
    def Metodo_obbligatorio(self):
        pass

class Pippo_reale(Pippo_Astratto):
    
    def Metodo_obbligatorio(self):
        print("sono reale")
        
#finire di copiare l'esempio di astrazione, sono su github
        


