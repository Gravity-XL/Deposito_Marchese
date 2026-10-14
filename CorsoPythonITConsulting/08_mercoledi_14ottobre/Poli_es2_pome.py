

#1 classe padre

#3 variabili 6 get e set, il getter non deve riportare fila e numero, ma se un posto chiesto è occupato o libero 

#4 metodi, aggiungi posto, prenota posto, diche tipo? e poi deve stampare i posti liberi

#consiglio fare solo 3 file e 3 posti così è più facile da ragionare

#2 classi figlie, posto vip e posto standard, posto vip è un extra 

#posto standard: il posto normale di base ci da il costo, 
#il metodo prenota deve cambiare, se un utente ha scelto 1 posto 1c ad esempio, non potrà sceglierlo un altro utente

#potremmo avere 3 liste false false false, ecc
#quando verranno prenotati li facciamo diventare true

#teatro non è imparentata con nessuno, ha solo liste dei posti, serve per il duck typing


#creiamo la classe princiaple posto


class Posto:
    
    def __init__(self,numero:int, fila:str):
        self._numero = numero  #trattuno per renderli privato perchè interessa sapere solo se true o false
        self._fila = fila
        self._occupato = False
    
    def prenota(self):
        if self._occupato == True:
            print("Questo posto è già occupato.")
        else:
            self._occupato = True  # Lo impostiamo a True PER OCCUPARLO ADESSO ORA!!! ho perso 18 ore per questa cagata, sono uno sciocco.
            print("Posto prenotato con successo.")
    
    
    #ora che il prenota è corretto, facciamo il libera a quesoo punto
    # se il posto è occupato (True), allora lo disdiciamo e lo facciamo tornare libero (False).
    #Altrimenti (se era già libero), diciamo che non c'era nessuna prenotazione da annullare.
    
    def libera(self):
        
        if self._occupato == True:
            self.occupato = False #LO LIBERIAMO REALMENTE QUI IL POSTO, ALTRE 18 ORE INUTILI.
            print("il posto è nuovamente libero")
            
        else:
            print("il posto è già libero")
    
    # i getter per leggere le variabili
    def get_numero(self):
        return self._numero

    def get_fila(self):
        return self._fila
    
    def get_occupato(self):
        return self._occupato
    
class PostoStandard (Posto):
    
    def __init__(self, numero, fila, costo):
        super().__init__(numero, fila)
        self.costo = costo 
        
    # Override di prenota per mostrare il costo, da rivedere bene
    def prenota(self):
        
        if self.get_occupato() == True:
            print(f"posto standard {self.get_numero()}{self.get_fila()} è già occupato.") #è già occupatoquindi entra qui altrimeti
        
        else:
            # Sfruttiamo il metodo del padre per occuparlo REALMENTE, concetto confusionario ma da
            super().prenota()
            print(f"Costo totale addebitato: {self._costo}€")