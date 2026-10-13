
#classe base
class Animale:
    
    def __init__(self, nome):
        self.nome = nome
        
    def parla(self):
        print(f"{self.nome} fa un suono generico.")
    
#classe derivata (eredita da Animale)

class Cane(Animale):
    
    def parla(self):
        print(f"{self.nome} abbaia!")

animale_generico = Animale("AnimaleGenerico")
cane = Cane("Fido")

animale_generico.parla() #output: AnimaleGenerico fa suono generico.
cane.parla() #output: Fido abbaia!

#_____
# 
class Veicolo:
    def __init__(self, marca, modello):
        self.marca = marca
        self.modello = modello

def mostra_informazioni(self):
    print(f"Veicolo marca {self.marca}, modello {self.modello}")

class DotazioniSpeciali:
    def __init__(self, dotazioni):
        self.dotazioni = dotazioni

    def mostra_dotazioni(self):
        print(f"Dotazioni speciali: {', '.join(self.dotazioni)}")
        
        
        
class AutomobileSportiva(Veicolo, DotazioniSpeciali):

    def __init__(self, marca, modello, dotazioni, cavalli):
        Vincolo.__init__(self, marca, modello)
        #alternativa a super per l'ereditarietà multipla
        DotazioniSpeciali.__init__(self,dotazioni)
        self.cavalli = cavalli
        
    def mostra_informazioni(self):
        super().mostra_informazioni()
        #chiamiamo il metodo della prima superclasse
        print(f"Potenza: {self.cavalli} CV")
        self.mostra_dotazioni()
        #possiamo chiamare metodi di entrambe le superclassi
        
        
"""Creiamo un0istanza della classe AutomobileSportiva e utilizziamo i suoi metodi
per mostrare le informazioni sull'auto, inclusi i dettagli ereditati e quelli
specifici della classe """

auto_sportiva = AutomobileSportiva("Ferrari", "F8", ["ABS", "Controllo trazione", "Airbag laterali"], 720) 

auto_sportiva.mostra_informazioni()      