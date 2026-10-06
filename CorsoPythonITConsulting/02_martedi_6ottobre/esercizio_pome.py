#es 3
    
list1 = [1,2,3,4,5]  #scelgo la lista degli interi
    
list2 = ["Luca", "Mirko", "Pino"] #scelgo quella delle stringhe 
    
scelta = input("Scegli una lista: ")  #faccio a scegliere all'utente

if scelta == "list1":
    scelta2 = input("Vuoi aggiungere o rimuovere un numero? ") 

    if scelta2 == "aggiungere": 
        scelta = input("Cosa vuoi aggiungere? ") #possiamo usare scelta senza un'altra variabile visto che in questo blocco di codice c'è una volta
        list1.append(scelta)

    elif scelta2 == "rimuovere":
        scelta = int(input("Cosa vuoi rimuovere? "))
        list1.remove(scelta)

elif scelta == "list2":
    scelta2 = input("Vuoi aggiungere o rimuovere una parola? ")

    if scelta2 == "aggiungere":
        scelta = input("Cosa vuoi aggiungere? ")
        list2.append(scelta)

    elif scelta2 == "rimuovere":
        scelta = input("Cosa vuoi rimuovere? ")
        list2.remove(scelta)

else:
    print("Scelta non valida")

print(list1)
print(list2)