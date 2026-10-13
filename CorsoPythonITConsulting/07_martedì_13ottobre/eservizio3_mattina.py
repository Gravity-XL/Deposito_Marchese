

class Prodotto: #creo la classe padre del prodotto
    
    # Questa classe contiene gli attributi e i metodi comuni
# a tutti i prodotti che la fabbrica può vendere.

# DEFINISCO IL COSTRUTTORE DELLA CLASSE.
    # Il metodo __init__ viene eseguito automaticamente
    # quando creo un nuovo oggetto della classe. 
    # self è l'oggetto che sto creando.
    # Gli altri parametri sono i dati che passo all'oggetto.
    
    def __init__(self,nome, costo_produzione, prezzo_vendita):
        self.nome = nome 
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita
        
        
    #DEFINISCO IL METODO PER CALCOLARE IL PROFITTO.   
    #è un metodo di istanza perchè usa self
    def calcola_profitto(self):
        return self.prezzo_vendita - self.costo_produzione # RESTITUISCO IL RISULTATO DEL CALCOLO
    
class Elettronica(Prodotto): #CREO LA CLASSE FIGLIA Elettronica.
# Le parentesi indicano che Elettronica eredita da Prodotto. DA NON DIMENTICARE.
# In questo modo posso utilizzare gli attributi comuni, garanzia invece me lo sono aggiunto solo in elettronica
# e il metodo calcola_profitto() della classe padre.
    def __init__(self, nome, costo_produzione, prezzo_vendita, garanzia):
        super().__init__(nome, costo_produzione, prezzo_vendita)
        self.garanzia = garanzia
        
        #domanda fatta a mirko, da ricordare! con il super mi richiamo nome, cp e pv, mentre l'attributo dell'oggetto garanzia me lo assegno visto che è solo in questa classe (idem sotto per materiale)
        
class Abbigliamento(Prodotto): #questo ha lo stesso IDENTICO principio di quello di sopra
    def __init__(self, nome, costo_produzione, prezzo_vendita, materiale):
        super().__init__(nome, costo_produzione, prezzo_vendita)
        self.materiale = materiale
      
      
      
#CREO IL PRIMO OGGETTO della classe Elettronica.
# Articolo1 è la variabile che identifica l'oggetto.
# I valori passati sono nome, costo, prezzo e garanzia.
     
Articolo1 = Elettronica ("Plasytation 5", 200, 600, 1)
Articolo2 = Abbigliamento ("Cappotto", 37, 200,"lana")
Articolo3 = Elettronica ("Computer", 750, 1200, 2)


#CALCOLO E STAMPO IL PROFITTO del primo prodotto.
# Richiamo il metodo ereditato da Prodotto.

print(Articolo1.calcola_profitto())
print(Articolo2.calcola_profitto())
print(Articolo3.calcola_profitto())

#tutto risolto

