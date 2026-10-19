

#from abc import ABC, abstractmethod  #importiamo una classe e un decoratore #dalla libreria abc importami abstract method

#non può diventare un oggetto, il decoratore ti permette di lasciare metodi vuoti e costringere i figli a sovrascrivere

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

#ogni metodo astratto dve essere implementato nella classe figlio

#1 metodo astratto? classe figlia 1 metodo astratto

#cosa in più, può contenere anche abstractmethod
#la cosa in meno, non può diventare un oggetto

#decoratore si potrà mettere solo nelle funzioni che mettiamo noi

#metodo stratto che dichiariamo con il metodo astratto NON PUO' AVERE UN CORPO

#possono avere tutto il resto

#USARLO COME RIFERIMENTO, DARE IL TIPO A TUTTI GLI ALTRI ELEMENTI

#LA COSA CHE HA IN PIù LA POSSIBILITà DI CREARE METODI VUOTI DA RIEMPIRE PER I FIGLI

#anche per robustezza, ogni figlio dobrà implementare "aria e perimetro", sto obbligando l'ereditarietà a farmi decidere le cose a me
#SERVE A CREARE ELEMENTI DINAMICI


