# step1_ chiedere un numero all'utente

numero = int(input("inserisci un numero: "))

x = numero #mi dichiaro x che è uguale a numero per utilizzarlo nel range

#quindi partendo da quel numero dobbiamo andare fino a zero, usiamo il for con il range

for i in range(x,-1, -1):
    print(i)
    
#aggiungengo lo stop a -1 mi stampa anche 0 ed ho inserito che lo step è -1 per stampare tutti i numeri

#a questo punto dobbiamo chiedere e vuole uscire o inserire un altro numero, uso il while

ripeti = "si"

while ripeti == "si":
    
    x = int(input("inserisci un altro numero: "))
    for i in range(x,-1, -1):
    
        print(i)
    
    ripeti = input("Vuoi inserire un altro numero? ")
   
   
    if ripeti != "si":
        print("Arrivederci")