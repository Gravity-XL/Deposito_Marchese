

class MembroSquadra:  #membro della squadra generico con nome ed età
    
    def __init__(self, nome, eta): #il costruttore 
        self.nome = nome 
        self.eta = eta
    
    def descrivi(self): #descrive il membro della squadra
        print(f"{self.nome},{self.eta} anni")
        
class Squadra: 
    
    def __init__(self, nome):
        self.nome = nome
        
    def gioca_contro(self, altra_squadra, vincitrice): #a questo punto self è la squadra che chiama il metodo ed ho messo l'avversaria
        print(f"{self.nome} vs {altra_squadra.nome}") 
        print(f"Ha vinto: {vincitrice.nome}")
    
class Giocatore(MembroSquadra): # Costruttore con gli attributi comuni e quelli specifici, domanda che feci a mirko per l'uso del super
    
    def __init__(self, nome, eta, ruolo, numero_maglia):
        super().__init__(nome, eta)
        self.ruolo = ruolo # Attributi specifici del giocatore, questi li devo mettere se non sono quelli comuni (collegato a domanda a mirko)
        self.numero_maglia = numero_maglia
        
    def gioca_partita(self):
        print(f"{self.nome} sta giocando come {self.ruolo}")

class Allenatore(MembroSquadra):
    # Costruttore con gli attributi comuni e quelli specifici, stessa storia di prima
    def __init__(self, nome, eta, anni_esperienza):
        super().__init__(nome, eta) #richiamo solito costruttore con super
        self.anni_esperienza = anni_esperienza #aggiunta attributo specifico
        
    def dirige_allenamento(self):
        print(f"{self.nome} dirige l'allenamento")


class Assistente(MembroSquadra): #identico ai precedenti
    def __init__(self, nome, eta, specializzazione):
        super().__init__(nome, eta)
        self.specializzazione = specializzazione
        
    def supporta_team(self): 
        print(f"{self.nome} supporta la squadra come {self.specializzazione}")    
        
        #creo oggetti squadre
squadra1 = Squadra("Inter")
squadra2 = Squadra("Milan")
     #faccio vincere spudoratamente il milan !!!
squadra1.gioca_contro(squadra2, squadra2)

