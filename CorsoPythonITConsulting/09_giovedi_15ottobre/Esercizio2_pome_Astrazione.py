

#una funzione che possa accettare 

#1 metodo solo che possa accettare 

#1 classe astratta impiegato con costruttore reale 
#LA CLASSE ASTRATTA CI PERMETTE LETTERALMENTE 
# DI OBBLIGARE LE CLASSI FIGLIE A RISPETTARE DELLE REGOLE CHE DECIDIAMO NOI


#IMPIEGATO CHE LA CLASSE ASTRATTA, è UNA SORTA DI MODELLO COMUNE
#NOME, COGNOME, STIPENDIO BASE
#CALCOLO STIPENDIO
#IMPIEGATO FISSO (STIPENDIO BASE INVARIATO)
#IMPIEGATO A PROVVIGIONE STIPENDIO BASE + BONUS DELE VENDIT

#DICIAMO CEH POSSIAMO DIRE : l'astrazione diventa utile qui perchè: 
# noi decidiamo la regola comune, mentre ogni classe figlia decide come applicarla.


from abc import ABC, abstractmethod


# CLASSE ASTRATTA
class Impiegato(ABC):

    # Costruttore: inizializza i dati comuni a tutti gli impiegati, molto basic
    def __init__(self, nome, cognome, stipendio):
        self.nome = nome
        self.cognome = cognome
        self.stipendio = stipendio

    # Metodo astratto: obbliga le classi figlie a implementarlo
    @abstractmethod
    def calcola_stipendio(self):
        pass


# CLASSE FIGLIA: IMPIEGATO FISSO
class ImpiegatoFisso(Impiegato):

    # Riceve i dati e li passa al costruttore della classe padre
    def __init__(self, nome, cognome, stipendio):
        super().__init__(nome, cognome, stipendio)

    # Implementa il metodo astratto: lo stipendio non cambia
    def calcola_stipendio(self):
        return self.stipendio


# CLASSE FIGLIA: IMPIEGATO A PROVVIGIONE
class ImpiegatoAProvvigione(Impiegato):

    # Oltre ai dati comuni, riceve il bonus sulle vendite
    def __init__(self, nome, cognome, stipendio, bonus):
        super().__init__(nome, cognome, stipendio)
        self.bonus = bonus

    # Implementa il metodo astratto con una logica diversa
    def calcola_stipendio(self):
        return self.stipendio + self.bonus  #potevo farlo con l'input


# FUNZIONE PER STAMPARE LE INFORMAZIONI
def stampa_impiegato(impiegato):
    print(f"Nome: {impiegato.nome}")
    print(f"Cognome: {impiegato.cognome}")
    print(f"Stipendio mensile: {impiegato.calcola_stipendio()} euro")
    print("-" * 30) #dacapire 


# CREIAMO GLI OGGETTI DELLE CLASSI FIGLIE
impiegato1 = ImpiegatoFisso("Luca", "Marchese", 2000)
impiegato2 = ImpiegatoAProvvigione("Dario", "Marchese", 3000, 500)

# Usiamo la stessa funzione per entrambi gli impiegati
stampa_impiegato(impiegato1)
stampa_impiegato(impiegato2)


       