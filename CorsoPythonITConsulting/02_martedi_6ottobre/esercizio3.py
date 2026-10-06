
lista = []  #creo lista buota

nome = input("inserisci il nome: ")  #inserisco valoti per tipo
eta = int(input("Inserisci l'eta: "))
sesso = input ("Inserisci il sesso (M o F): ")
premium = input ("Sei premium? ")

if premium == "si":  #if per convertire il booleano
    premium = True
else:
    premium = False
    

lista.append(nome)  #aggiungo nella lista i dati presi dall'input
lista.append(eta)
lista.append(sesso)
lista.append(premium)

scelta = input("Cosa vuoi modificare? (nome, eta, sesso, premium): ")  #variabile scelta mi permette di modificare cosa voglio modificare nell'input

match scelta:  #match scelgo i 4 casi, e nel premium sono in dubbio se ho fatto bene l'if nuovamente o non c'era bisogno di farlo (intendo il finale)

    case "nome":
        nome = input("Inserisci il nuovo nome: ")
        lista[0] = nome
        #print(lista)?
    case "eta":
        eta = int(input("Inserisci la nuova eta: "))
        lista[1] = eta
        #print(lista)
    case "sesso":
        sesso = input("Inserisci il nuovo sesso (M o F): ")
        lista[2] = sesso
        #print(lista)
    case "premium":
        premium = input("Sei premium? (si/no): ")

        if premium == "si":
            premium = True
        else:
            premium = False

        lista[3] = premium
        
print(lista)

#il codice funziona ma ho riscontato un problema, un controllo dei tipi, ad esempio al posto del nome se inserisco "2" mi da "2"