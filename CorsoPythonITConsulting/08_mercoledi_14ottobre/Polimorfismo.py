# esercizio 

 #4 classi, classe Padre, metodo pagamento, paypal, carta di credito, 

 #effettua pagamento nel padre
 #sovrascritture dei metodi per le classi figlie

 #ulteriore classe gestore pagamenti, metodo che

 #gestione pagamenti

 #non è richiesto l'incapsulamento, oppure come esercizio extra . ma per ora non la facciamo


class MetodoPagamento:
    
    def effettua_pagamento(self, importo):
       #print(f"Pagamento di {importo}€") #qnon so se ha senso collegarla 
       # al gestore pagamento visto che specifichrò l'importo direttamente dalle figlie
        pass #quando lo tolgo mi da errore subito dopo che scrivo class in metodo pagamento
class PayPal(MetodoPagamento):
    
    def effettua_pagamento(self, importo):
        print(f"Pagamento di {importo}€ tramite PayPal")

class CartaDiCredito(MetodoPagamento):
    
    def effettua_pagamento(self, importo):
        print(f"Pagamento di {importo}€ tramite Carta di Credito")
        
class GestorePagamenti:
    
    def gestisci_pagamento(self, metodo_scelto:object, importo:int):
        metodo_scelto.effettua_pagamento(importo)        
        
        
        # 1. Creiamo l'istanza del nostro Gestore
cassa = GestorePagamenti()

# 2. Creiamo i nostri due metodi di pagamento pronti all'uso
account_paypal = PayPal()
mia_carta = CartaDiCredito()

# 3. Facciamo i pagamenti passandoli al gestore!
print("--- Simulazione dei pagamenti ---")
cassa.gestisci_pagamento(account_paypal, 50)  # Utilizza PayPal
cassa.gestisci_pagamento(mia_carta, 50)     # Utilizza la Carta di Credito
