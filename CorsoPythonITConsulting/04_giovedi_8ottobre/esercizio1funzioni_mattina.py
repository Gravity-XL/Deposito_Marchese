

#ERRORE DA RICORDARE a = int(input("Scegli un numero da far indovinare: ")) 
#LASCIARE QUELLA RIGA TI FA INSERIRE DUE VOLTE IL NUMERO DA INDOVINARE, NON HA SENSO USARLO ADESSO 


def indovina(a):  #dichiaro "a" nella funzione ma ancora non ha un valore 

    while True:
        numero = int(input("Indovina il numero: "))  #chiediamo all'utente il numero da indovinare

        if numero == a:  #ovviamente faccio l'if, se è uguale, ho indovinato, maggiore o minore 
            print("Hai indovinato!")
            break

        elif numero < a:
            print("Il numero da indovinare è più alto.")

        elif numero > a:
            print("Il numero da indovinare è più basso.")
            
        scelta = input("Vuoi fare un altro tentativo? ") 
        
        if scelta == "no":
            print("Arrivederci")
            break
        
        #AVEVO MANCATO LA SCELTA, L'UTENTE DEVE AVERE LA POSSIBILITà DI POTER USCIRE

while True: 

    x = int(input("Scegli un numero da indovinare: ")) # x ivece me lo dichiaro come numero che deve indovinare l'utente

    indovina(x) #la funzione indovina fa svolgere la appunto la funzione di sopra e fa il confronto con il while che ho fatto prima

    scelta = input("Vuoi rigiocare? ")  #scelta veloce vuoi rigiocare "si" se no "arrivederci e grazie :-)"

    if scelta == "no":
        print("Arrivederci")
        break
    
    #ho fatto varie prove ed ho notato che se dico che non voglio fare un altro tentativo, mi dice arrivederci e poi se voglio rigiocare
    #come se uscissi prima dal livello. e poi proprio dal gioco (facendo l'esempio di un gioco)
    #da risolvere quindi la scelta dell'utente, se non vuole riprovare voglio che esce direttamente senza richiedermelo