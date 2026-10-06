x = int(input("inserisci un numero "))

if x < 5:
    
    x = int(input("il numero è minore di 5, inserisci un numero maggiore di 5:"))
    if x < 8:
       
        x = int(input("il numero è minore di 8, inserisci un numero maggiore di 8:"))
        if x ==20:
            print("wow hai scelto 20")
        else: 
            print("hai inserito ", x)
        
        
# es 2


lista = [1,2,3] #ho una lista di 3 numeri

scelta = input("cosa vuoi fare?") #l'utente sceglierà se aggiungere, rimuovere o modificare

if scelta == "aggiungi" : #se sceglie la prima scelta aggiungi, entra in questo if e aggiunge una parola alla fine della lista
    scelta2 = input("scegli una parola") #inseriamo la parola che vogliamo
    lista.append(scelta2) #aggiunge la parola letteralmente
    
    print(lista) 
elif scelta == "rimuovi": #questo blocco di docie invece ti permettere di rimuovere il numero in questo caso
    print("scegli cosa rimuovere fra: ", lista)
    scelta2 = input("scegli un numero: ")
    lista.remove(scelta2)
    
    print(lista)  
elif scelta == "modifica": #questo blocco di codice ti permette di modificare nella posizione che vogliamo una parola scritta dall'input, nella posizioen che scegliamo dall'input
    print("scegli quale posizione modificare da 0 con limite a", len(lista)-1 )
    scelta2 = int(input("scegli una posizione: "))
    scelta3 = input("scegli una parola da aggiungere: ")
    lista[scelta2] = scelta3
    
    print(lista)   
else: #nessuna delle scelte precedenti è giusta, quindi stampa scelta sbagliata
    print("Scelta sbagliata")
    
    
    
    