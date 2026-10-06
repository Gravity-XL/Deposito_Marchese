eta = int(input("Inserisci la tua età: "))
maggiorenne = eta >= 18

if maggiorenne == True:
    #eta = "maggiorenne"
    print("Puoi vedere questo film")
else:
    eta = False
    print("Mi dispiace, non puoi vedere questo film")