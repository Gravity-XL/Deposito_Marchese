

class Animale: #classe animale

    numero_animali = 0 #attributo di classe che parte da zero, incrementerà quando aggiungeremo animali


    #il costruttore che verrà eseguito automaticamente appena creiamo l'oggetto nuovo 
    def __init__(self, nome, specie):
        #i due attributi di istanza, con nome e specie
        self.nome = nome
        self.specie = specie
        Animale.numero_animali += 1 #semplice contatore che incrementa di 1 ogni volta che creiamo un aniamle
        
    # Decoratore che definisce un metodo di classe
    @classmethod
    def quanti_animali(cls):
        # cls rappresenta la classe Animale
        # Stampa il valore attuale del contatore condiviso
        print("numero animali creati:", cls.numero_animali)
#questi sono i 3 oggetti della classe animale e ogni creazione esegue init e aumena il contatore            
animale1 = Animale("Zeus", "Cane")        
animale2 = Animale("Spike", "Cane") 
animale3 = Animale("Virgola", "Gatto")  

# Chiamiamo il metodo direttamente dalla classe, senza usare un'istanza
Animale.quanti_animali()