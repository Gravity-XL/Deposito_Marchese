# GESTIONE DI PRODUZIONE DI UNA FABBRICA

"""Scrivi un programma che simula una piccola gestione della produzione di una fabbrica.

La fabbrica produce pezzi e il programma deve permettere all'utente di registrare i prodotti realizzati durante la giornata.

Ogni prodotto sarà rappresentato solo dal nome del prodotto e dalla quantità prodotta.

il programma deve mostrae un menu continuo che si ripete fino a quando l'utente decide di uscire

Menu richiesto

1. aggiungi prodotto
2. visualizza produzione
3. cerca prodotto
4. modifica quantità
5. rimuovi prodotto
6. calcola totale pezzi prodotti
7. esci """


#padre_ classe prodotto  (nome, num_pezzi) #figlia1_classe magliette,  #figlia2_classe jeans 
#magari classe per gestire il tutto, gestione produzione con metodo registra i prodotti realizzati da nome prodotto e quantita (es magliette,12 - jeas,20) 
# metodo aggiungi,metodo modifica,metodo rimuovi, calcola totale (che potrebbe essere la somma della produzione delle due classi) stampa produzione, magari alla fine del calcolo del totale dei przzi
#menu alla fine


class Prodotto: #classe padre con get e set, senza accedere direttamente quindi
    
    def __init__(self, nome, quantita): #costruttore che inizializza nome e quantità
        self.__nome = nome
        self.__quantita = quantita
        
    def get_nome(self):
        return self.__nome

    def get_quantita(self):
        return self.__quantita
    
    def set_nome(self, nuovo_nome):
        self.__nome = nuovo_nome

    def set_quantita(self, nuova_quantita):
        self.__quantita = nuova_quantita
    
class Maglietta(Prodotto): #a questo punto eredito tutto da prodotto 
    
    pass     
        
class Jeans(Prodotto):
    
    pass         

class GestioneProduzione: #lista vuota da riempire man mano e fa le operazioni sui prodotti
    
    def __init__(self):
        self.lista = []
    
    def aggiungi_prodotto(self, nome, quantita, tipo): #crea un prodotto del tipo scelto e lo aggiunge alla lista
        if tipo == "maglietta":
            prodotto = Maglietta(nome, quantita)
        elif tipo == "jeans":
            prodotto = Jeans(nome, quantita)

        self.lista.append(prodotto)
        
    def visualizza_produzione(self): #mostra tutti i prodotti presenti nella lista
            if not self.lista:
                print("Nessun prodotto presente")
            else:
                for prodotto in self.lista:
                    print(f"Nome: {prodotto.get_nome()} | Quantità: {prodotto.get_quantita()}")
    
    def cerca_prodotto(self, nome): #cerca un prodotto peril nome e restituisce l'oggett o trovato
        for prodotto in self.lista:
            if prodotto.get_nome() == nome:
                print(f"Nome: {prodotto.get_nome()} | Quantità: {prodotto.get_quantita()}")
                return prodotto

        print("Prodotto non trovato")
        return None
    
    def modifica_quantita(self, nome, nuova_quantita): #cerca il prodotto e ne aggiorna la quantità
        prodotto = self.cerca_prodotto(nome)

        if prodotto is not None:
            prodotto.set_quantita(nuova_quantita)
            print("Quantità modificata!")

    def rimuovi_prodotto(self, nome): #cerca il prodotto e lo elimina dalla lista
        prodotto = self.cerca_prodotto(nome)

        if prodotto is not None: #is not none per vedee se il prodot è pres reakmente
                self.lista.remove(prodotto)
                print("Prodotto rimosso!")

    def totale_pezzi(self): #somma le quantità di tutti i prodotti presenti nella lista
        totale = 0

        for prodotto in self.lista:
            totale += prodotto.get_quantita()

        print(f"Totale pezzidei prodotti: {totale}")


# MENU PRINCIPALE

gestione = GestioneProduzione()  #crea l'oggetto che gestisce la produzione

while True: #ripete il menu fino a quando l'utente sceglie di uscire
    
    print("\n--- GESTIONE PRODUZIONE ---")
    print("1. Aggiungi prodotto")
    print("2. Visualizza produzione")
    print("3. Cerca prodotto")
    print("4. Modifica quantità")
    print("5. Rimuovi prodotto")
    print("6. Calcola totale pezzi prodotti")
    print("7. Esci")

    scelta = input("Scegli un'opzione: ") 

    if scelta == "1":
        nome = input("Nome prodotto: ")
        quantita = int(input("Quantità: "))
        tipo = input("Tipologia (maglietta/jeans): ").lower()

        gestione.aggiungi_prodotto(nome, quantita, tipo)

    elif scelta == "2":
        gestione.visualizza_produzione()

    elif scelta == "3":
        nome = input("Nome prodotto da cercare: ")
        gestione.cerca_prodotto(nome)

    elif scelta == "4":
        nome = input("Nome prodotto da modificare: ")
        nuova_quantita = int(input("Nuova quantità: "))
        gestione.modifica_quantita(nome, nuova_quantita)

    elif scelta == "5":
        nome = input("Nome prodotto da rimuovere: ")
        gestione.rimuovi_prodotto(nome)

    elif scelta == "6":
        gestione.totale_pezzi()

    elif scelta == "7":
        print("Programma terminato!")
        break

    else:
        print("Scelta non valida!")

    
