lista = [] 

def inserisci(): #faccio la funzione inserisci con l'input così posso inserire sempre cose
    valore = input("Inserisci un valore: ")
    lista.append(valore)
    print("Valore inserito!")

def modifica():  #questo blocco lo uso per modificare, non sono riuscito a costruire io tutta la logica, mi sono aiutato con internet
    print(lista)
    posizione = int(input("Quale posizione vuoi modificare? "))
    if posizione >= 0 and posizione < len(lista):
        valore = input("Inserisci il nuovo valore: ")
        lista[posizione] = valore
        print("Lista aggiornata")
    else:
        print("Posizione non valida")
        
        #il dubbio che ho avuto qui è creare quel "posizione", non avevo valutato, guardando esempi e blocchi di codice diversi ho preso spunto per farmi la posizione e farlo scorere

def stampa():
    print(lista)

#a questo punto ho usato posizione anche di qua, il pop invece lo avevo completamente rimosso, l'ho cercato su internet
#in realtà ho provato remove ma non funzionava 
def elimina():
    print(lista)
    posizione = int(input("Quale posizione vuoi eliminare? "))
    if posizione >= 0 and posizione < len(lista):
        lista.pop(posizione)
        print("Elemento eliminato!")
    else:
        print("Posizione non valida")

while True:
    print("\n1. Inserisci")
    print("2. Modifica")
    print("3. Stampa")
    print("4. Elimina")
    print("5. Esci")

    scelta = input("Scegli un'opzione: ")

#qui ero indeciso se usare match o if, ma così funziona
    if scelta == "1":
        inserisci()
    elif scelta == "2":
        modifica()
    elif scelta == "3":
        stampa()
    elif scelta == "4":
        elimina()
    elif scelta == "5":
        break
    else:
        print("Scelta non valida")