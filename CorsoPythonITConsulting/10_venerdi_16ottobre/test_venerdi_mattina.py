""" Esercizio: Gestionale di un’Officina di Elettrodomestici
Concetti obbligatori: incapsulamento, ereditarietà, polimorfismo, uso di type() per controllare
gli oggetti e metodi “variatici” (con parametri variabili).
Stai progettando il software di base per un’officina che si occupa di riparare elettrodomestici
(lavatrici, frigoriferi, forni, ecc.). Il programma dovrà modellare gli elettrodomestici, i
ticket di riparazione e alcune operazioni dell’officina, usando la programmazione ad oggetti.
1. Classe base: Elettrodomestico
Crea una classe base chiamata Elettrodomestico che rappresenti un elettrodomestico generico.
Attributi (incapsulati, cioè privati):
__marca (stringa)
__modello (stringa)
__anno_acquisto (intero)
__guasto (stringa che descrive il problema principale)
Metodi:
Costruttore __init__(self, marca, modello, anno_acquisto, guasto)
Getter e setter per tutti gli attributi, con eventuali controlli minimi (es. l’anno non può essere nel
futuro).
descrizione(self): restituisce una stringa con marca, modello, anno e guasto.
stima_costo_base(self): restituisce un valore numerico generico (es. costo base di diagnosi).
Regola 1 – Incapsulamento: tutti gli attributi devono essere privati (__attributo) e accessibili solo
tramite getter/setter.
2. Classi derivate (Ereditarietà + Polimorfismo)
Crea almeno tre sottoclassi di Elettrodomestico:
1.Lavatrice
Attributi aggiuntivi:
capacita_kg (intero)
giri_centrifuga (intero)
Override di stima_costo_base(self): la lavatrice ha un costo base diverso (ad esempio, maggiorato se
la capacità è elevata).
2.Frigorifero
Attributi aggiuntivi:
litri (intero)
ha_freezer (booleano)
Override di stima_costo_base(self): il costo può cambiare se ha il freezer o se i litri superano una
certa soglia.
3.Forno
Attributi aggiuntivi:
tipo_alimentazione (stringa: “elettrico”
,
“gas”)

ha_ventilato (booleano)
Override di stima_costo_base(self): il costo può cambiare in base al tipo di alimentazione e alla
presenza della funzione ventilata.
Regola 2 – Ereditarietà: tutte le classi derivate devono usare Elettrodomestico come classe base ed
ereditare i suoi attributi tramite super() nel costruttore.
Regola 3 – Polimorfismo: tutte le sottoclassi devono fornire la propria versione di
stima_costo_base(self), in modo che la chiamata a questo metodo su una lista mista di oggetti (Lavatrice,
Frigorifero, Forno) produca risultati diversi a seconda del tipo.

3. Classe TicketRiparazione
Crea una classe TicketRiparazione che rappresenta un ticket aperto in officina.
Attributi (incapsulati):
__id_ticket (intero o stringa univoca)
__elettrodomestico (un oggetto di tipo Elettrodomestico o sottoclasse)
__stato (stringa: “aperto”, “in lavorazione”, “chiuso”)
__note (lista di stringhe, inizialmente vuota)
Metodi:
Costruttore __init__(self, id_ticket, elettrodomestico)
Getter e setter necessari (ad esempio per stato e note).
aggiungi_nota(self, testo) per aggiungere una nota.
calcola_preventivo(self, *voci_extra) → metodo variadico:
usa elettrodomestico.stima_costo_base() come costo di partenza
somma tutte le voci extra passate come parametri (*voci_extra)
restituisce il totale.
Nota: questo metodo deve funzionare con qualsiasi sottoclasse di Elettrodomestico
(polimorfismo sul metodo stima_costo_base).

4. Classe Officina
Crea una classe Officina che gestisce i ticket e gli elettrodomestici.
Attributi:
nome (stringa)
tickets (lista di oggetti TicketRiparazione)
Metodi:
aggiungi_ticket(self, ticket)
chiudi_ticket(self, id_ticket)
stampa_ticket_aperti(self): mostra ID, tipo di elettrodomestico e stato.
totale_preventivi(self): somma i preventivi di tutti i ticket.
5. Uso di type() e controllo degli oggetti
All’interno della classe Officina (o in una funzione separata) implementa un
metodo, ad esempio:
statistiche_per_tipo(self)
Questo metodo deve:
Iterare su tutti i ticket.
Usare type() (oppure isinstance()) per capire se l’elettrodomestico associato
al ticket è una Lavatrice, un Frigorifero o un Forno.
Contare quanti ticket ci sono per ciascuna sottoclasse.
Stampare un piccolo report, per esempio:
“Numero di lavatrici in riparazione: X”
“Numero di frigoriferi in riparazione: Y”
“Numero di forni in riparazione: Z”
Requisito: il metodo deve utilizzare type() (o, come variante consigliata,
isinstance()) per differenziare in base al tipo reale degli oggetti.   """

#ragionamento sulla struttura prima di tutto

#facciamo la classe elettrodomestico come classe padre e attributi privati con metodi comuni
#ereditarietà con super()
#lavatrice, frigorifero, forno (costi personalizzati)
# l'incapsulamento ce lo facciamo con gli attributi della classe padre, e ci accediamo attraverso getter e setter
#ereditarietà: ce lo facciamo sulle sottoclassi 
#polimorfismo ogni sottoclasse si fa per fatti suoi la propria stima del costo base
#DA SCEGLIERE, CI RAGIONO DOPO, metodo che varia non so se fargli raccogliere i costi aggiuntivi in una variabile o in una lista e poi li sommiamo semplicemente
#TYPE DA RIVEDERE, lo userei solo per riconoscere che tipo di elettrodomestico scegliamo (potevo usarlo anche esercizio di ieri effettivametnte) DA RAGIONARCI SOPRA à
#officina facciamo il conteggio della lista dei ticket e si occuperò della gestione dei ticket appunto

#costi base magari li scegliamo random


from abc import ABC, abstractmethod


class Elettrodomestico(ABC): #classe padre costruttore fatta, e attributi privati all'interno
    
    def __init__(self, marca, modello, anno_acquisto, guasto):
        self.__marca = marca
        self.__modello = modello
        self.__anno_acquisto = anno_acquisto
        self.__guasto = guasto
        
    #faccio direttamente getter e setter per leggere, modificare gli attributi e assegnamo direttamente il nuovo valore, nel setter anno diacquisto ricordati di impdire l'acquisto nell'anno sbagliato)
    def get_marca(self):
        return self.__marca

    def get_modello(self):
        return self.__modello

    def get_anno_acquisto(self):
        return self.__anno_acquisto

    def get_guasto(self):
        return self.__guasto
    

    def set_marca(self, marca):
        self.__marca = marca

    def set_modello(self, modello):
        self.__modello = modello

    def set_anno_acquisto(self, anno_acquisto):
        if anno_acquisto <= 2026:
            self.__anno_acquisto = anno_acquisto
        else:
            print("Errore: anno di acquisto non valido.")

    def set_guasto(self, guasto):
        self.__guasto = guasto
    
    
    # descrizione ci facciamo mandare semplicemente le info dell'elett.
    # mentre stima e costo È ASTRATTO, OGNI CLASSE FIGLIA DOVRA' IMPLEMENTARLO CON IL PROPRIO CALCOLO, DA NON DIMENTICAR
    

    def descrizione(self):
        return (
            f"Marca: {self.__marca}, "
            f"Modello: {self.__modello}, "
            f"Anno: {self.__anno_acquisto}, "
            f"Guasto: {self.__guasto}"
        )

    # metodo astratto della stima del costo che metteremo IN OGNI CLASSE FIGLIA PER FORZA

    @abstractmethod
    def stima_costo_base(self):
        pass

"""Crea almeno tre sottoclassi di Elettrodomestico:
1.Lavatrice
Attributi aggiuntivi:
capacita_kg (intero)
giri_centrifuga (intero)
Override di stima_costo_base(self): la lavatrice ha un costo base diverso (ad esempio, maggiorato se
la capacità è elevata).
2.Frigorifero
Attributi aggiuntivi:
litri (intero)
ha_freezer (booleano)
Override di stima_costo_base(self): il costo può cambiare se ha il freezer o se i litri superano una
certa soglia.
3.Forno
Attributi aggiuntivi:
tipo_alimentazione (stringa: “elettrico”"""



class Lavatrice (Elettrodomestico): #lavatrice eredita dalla classe padre e inizializza l'attrivuto privato capacita_kg
    
    def __init__ (self, marca, modello, anno_acquisto, guasto, capacita_kg):
        super().__init__(marca, modello, anno_acquisto, guasto)
        self.__capacita_kg = capacita_kg
        
    # get e set anche di capacità kg naturalmetne

    def get_capacita_kg(self):
        return self.__capacita_kg

    def set_capacita_kg(self, capacita_kg):
        self.__capacita_kg = capacita_kg

    # implemento metodo astratto
    #(ultime lezioni), classe padre ha dichiarato COSA DEVE ESISTERE,  classe figlia VA A DEFINIRE QUEL METODO !!!
    #questo è il motivo palese perche anche le altre classi figlie forno e frigorifero potranno avere tutti stima_costo_base()
    #ma ciharamente calcolare i costi in modi diversi, esattamente il POLIMORFISMO!!!

    def stima_costo_base(self): #prendiamo il metodo dichiarato nel padre e gli diamo un comportamento concreto nella figlia.
        costo = 50

        if self.__capacita_kg > 8:
            costo += 20

        return costo

class Frigorifero (Elettrodomestico): #classe figlia con solito costruttore con attributi personlizzati in bae alla classe in questione
    
    def __init__(self, marca, modello, anno_acquisto, guasto, ha_freezer, litri):
        super().__init__(marca, modello, anno_acquisto, guasto)
        self.__ha_freezer = ha_freezer
        self.__litri = litri

     # soliti get e set

    def get_ha_freezer(self):
        return self.__ha_freezer

    def set_ha_freezer(self, ha_freezer):
        self.__ha_freezer = ha_freezer

    def get_litri(self):
        return self.__litri

    def set_litri(self, litri):
        self.__litri = litri

    # solito metodo astratto personalizzato al frigo chiaramente (riguardare regola scritta sopra nei commenti nel dubbio)

    def stima_costo_base(self):
        costo = 50

        if self.__ha_freezer:
            costo += 15

        if self.__litri > 300:
            costo += 20

        return costo
    

class Forno (Elettrodomestico):
    
    def __init__(self, marca, modello, anno_acquisto, guasto, alimentazione_gas, ventilato):
        super().__init__(marca, modello, anno_acquisto, guasto)
        self.__alimentazione_gas = alimentazione_gas
        self.__ventilato = ventilato
        
    # get set

    def get_alimentazione_gas(self):
        return self.__alimentazione_gas

    def set_alimentazione_gas(self, alimentazione_gas):
        self.__alimentazione_gas = alimentazione_gas

    def get_ventilato(self):
        return self.__ventilato

    def set_ventilato(self, ventilato):
        self.__ventilato = ventilato

    # astratto

    def stima_costo_base(self):
        costo = 50

        if self.__alimentazione_gas:
            costo += 10

        if self.__ventilato:
            costo += 15

        return costo


"""4. Classe Officina
Crea una classe Officina che gestisce i ticket e gli elettrodomestici.
Attributi:
nome (stringa)
tickets (lista di oggetti TicketRiparazione)
Metodi:
aggiungi_ticket(self, ticket)
chiudi_ticket(self, id_ticket)
stampa_ticket_aperti(self): mostra ID, tipo di elettrodomestico e stato.
totale_preventivi(self): somma i preventivi di tutti i ticket."""




class TicketRiparazione: #attrivuti nuovi inseriti, ed elettrodomestico così può essere uno dei 3 tra lavatrice frigo e forno

    def __init__(self, id_ticket, elettrodomestico):
        self.__id_ticket = id_ticket #salviamo l'id
        self.__elettrodomestico = elettrodomestico #salva l'obj da riparare
        self.__stato = "aperto" #allo start il tiket è aperto
        self.__note = []
        
    # get e set per accederci

    def get_id_ticket(self):
        return self.__id_ticket

    def get_elettrodomestico(self):
        return self.__elettrodomestico

    def get_stato(self):
        return self.__stato

    def get_note(self):
        return self.__note

    # Set

    def set_id_ticket(self, id_ticket):
        self.__id_ticket = id_ticket

    def set_elettrodomestico(self, elettrodomestico):
        self.__elettrodomestico = elettrodomestico

    def set_stato(self, stato):
        if stato in ["aperto", "in lavorazione", "chiuso"]:
            self.__stato = stato
        else:
            print("Errore: stato non valido.")

    def set_note(self, note):
        self.__note = note


#la nota facciamola semplice con append, lo aggiungiamo alla lista e il calcolo preventivo i costi 

    def aggiungi_nota(self, nota):
        self.__note.append(nota)
    
    def calcola_preventivo(self, *voci_extra):
        totale = self.__elettrodomestico.stima_costo_base()

        for voce in voci_extra:
            totale += voce

        return totale
    
#la classe officina anche l'ho decisa di fare molto semplices olo nome e lista e i tickets che si aggiungono con append

class Officina:

    def __init__(self, nome): #lista semplice, nome etiket
        self.nome = nome
        self.tickets = [] 
        
    def aggiungi_ticket(self, ticket): #aggiungiamo alla lista il ticket
        self.tickets.append(ticket)

    def chiudi_ticket(self, ticket): #chiuso, str chiuso
        ticket.set_stato("chiuso") 
        
    def stampa_ticket_aperti(self): #praticamente scorriamo o ticket e stampiamo solo se lo staot è uguale ad "aperto"
        for ticket in self.tickets:
            if ticket.get_stato() == "aperto":
                print(ticket.get_id_ticket())
                print(ticket.get_elettrodomestico().descrizione())
                
    def totale_preventivi(self):
        totale = 0
        for ticket in self.tickets:
            totale += ticket.calcola_preventivo()
        return totale           
        
    def statistiche_per_tipo(self):
        
        lavatrici = 0
        frigoriferi = 0
        forni = 0

        for ticket in self.tickets:
            elettrodomestico = ticket.get_elettrodomestico()

            if type(elettrodomestico) == Lavatrice:
                lavatrici += 1
            elif type(elettrodomestico) == Frigorifero:
                frigoriferi += 1
            elif type(elettrodomestico) == Forno:
                forni += 1

        print("Lavatrici:", lavatrici)
        print("Frigoriferi:", frigoriferi)
        print("Forni:", forni)
        
        
        
        
lavatrice = Lavatrice("Bosch", "Serie 4", 2022, "Perde acqua", 9)
frigorifero = Frigorifero("Samsung", "Family", 2021, "Non raffredda", True, 350)
forno = Forno("Whirlpool", "AKP", 2023, "Non scalda", False, True)

ticket1 = TicketRiparazione(1, lavatrice)
ticket2 = TicketRiparazione(2, frigorifero)
ticket3 = TicketRiparazione(3, forno)

officina = Officina("Officina Casa")

officina.aggiungi_ticket(ticket1)
officina.aggiungi_ticket(ticket2)
officina.aggiungi_ticket(ticket3)

ticket1.aggiungi_nota("Controllare il tubo")

print("TICKET APERTI:")
officina.stampa_ticket_aperti()

print("PREVENTIVI TOTALI:", officina.totale_preventivi())


#committo ora per il tempo finito e putroppo sono assente nel pomeriggio