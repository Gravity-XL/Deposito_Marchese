
class ContoCorrente:
    
    def __init__(self, intestatario, saldo):
        self.intestatario = intestatario
        self.saldo = saldo
        
    def deposita(self, importo):
        if importo > 0:
            self.saldo += importo
        else:
            print("Importo non valido")
                
    def ritira(self, importo):
        if importo > 0:
            self.saldo -= importo
        
            
    def visualizza(self):
        
scelta = ""
while scelta != "end" :
    pass


#####_

class ContoCorrente:

    # Costruttore della classe: inizializza intestatario e saldo
    def __init__(self, intestatario, saldo=0):
        self.intestatario = intestatario
        self.saldo = saldo

    # Metodo per depositare denaro sul conto
    def deposita(self, importo):  # Controlla che l'importo sia maggiore di zero
        if importo > 0:    # Aggiunge l'importo al saldo attuale
            self.saldo += importo
        else:
            print("Importo non valido")    # Mostra un errore se l'importo è zero o negativo

    # Metodo per prelevare denaro dal conto
    def ritira(self, importo): # Controlla che l'importo sia positivo e che il saldo sia sufficiente
        if importo > 0 and importo <= self.saldo:  # Sottrae l'importo dal saldo attuale
            self.saldo -= importo
        else:
            print("Importo non valido o saldo insufficiente")   # Mostra un errore se l'importo non è valido o il saldo è insufficiente

    # Metodo per visualizzare il saldo del conto
    def visualizza(self):
        # Stampa il nome dell'intestatario e il saldo attuale
        print(f"Il saldo di {self.intestatario} è: {self.saldo:.2f} euro")


# Chiede all'utente il nome dell'intestatario del conto
intestatario = input("Inserisci il nome dell'intestatario: ")

# Crea un oggetto della classe ContoCorrente con saldo iniziale pari a zero
conto = ContoCorrente(intestatario)

# Inizializza la variabile scelta
scelta = ""

# Ripete il menu finché l'utente non scrive "end"
while scelta != "end":

    # Mostra le operazioni disponibili
    print("\n--- MENU CONTO CORRENTE ---")  #\n per la new line, DA RICORDARE!!!
    print("1. Deposita")
    print("2. Preleva")
    print("3. Visualizza saldo")
    print("Scrivi 'end' per uscire")

    # Chiede all'utente quale operazione vuole eseguire
    scelta = input("Scegli un'operazione: ")


    if scelta == "1":
        importo = float(input("Inserisci l'importo da depositare: "))
        conto.deposita(importo)

    elif scelta == "2":
        importo = float(input("Inserisci l'importo da prelevare: "))
        conto.ritira(importo)

    elif scelta == "3":
        conto.visualizza()

    elif scelta == "end":
        print("Arrivederci!")

    else:
        print("Scelta non valida")