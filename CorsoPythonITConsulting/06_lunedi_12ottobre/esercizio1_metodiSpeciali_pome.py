class Garage: # ho definito la classe garage
    
    def __init__(self, capienza): #definisce il metodo costruttore
        self.capienza = capienza #è un attributo di istanza, mi serve per memorizzare la capienza massima del garage
        self.auto_presenti = [] #è un altro attributo di istanza #in questo caso la lista viene aggiunta in auto presenti direttamente dentro il costruttore, creerà una lista nuova per ogni nuovo garage
        #insomma conterà le auto parcheggiate
        
    def parcheggia(self, targa): #metodo per parcheggiare le auto, riceve come parametro la targa dell'auto da parcheggiare

        if targa in self.auto_presenti: #verifica se la targa è gia nella lista
            print("L'auto è già nel garage")

        elif len(self.auto_presenti) == self.capienza: #se la targa non è presente, verifica se il garage è pieno
            print("Il garage è pieno")

        else:
            self.auto_presenti.append(targa) #altrimenti aggiungi la targa alla lista
            print("Auto parcheggiata correttamente")
            
    def rimuovi(self, targa): #metodo per rimuovere l'auto, riceve come parametro l'auto da rimuovere
        
        #dice: se l'auto è presente in auto_presenti, allora rimuovi targa
        if targa in self.auto_presenti:
            self.auto_presenti.remove(targa)

        else: #se la targa non è presente, stampa che non è in garage
            print("L'auto non è nel garage")
            
    def posti_liberi(self): #metodi per calcolare posti liberi, semplicemente chiedo di far ritornare il risultato della capienza totale meno la "lunghezza" delle auto presenti 
        return self.capienza - len(self.auto_presenti)
    
    
garage1 = Garage(10) #creo l'oggetto garage, massio 10 auto e ne ho messe 2 randomicamente per provare a stampare posti_liberi

garage1.parcheggia("PR000VA")
garage1.parcheggia("PR001VA")

print(garage1.posti_liberi())

garage1.rimuovi("PR000VA")

print(garage1.posti_liberi())


#potrei aggiungere il menu con un semplice while, da prendere spunto esercizio 3_pome