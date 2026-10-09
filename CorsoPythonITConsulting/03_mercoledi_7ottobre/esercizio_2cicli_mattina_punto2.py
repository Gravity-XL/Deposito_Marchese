""" Punto2: utilizzo di while e range
Scrivi un sistema che prende in input un numero interno positivo n e stampa tutti i numeri da 0 a n (compreso), incrementando di 1
deve potersi ripetere all'infinito. """
""" 
numero = int(input("Scrivi un numero: "))

for i in range(0, numero + 1, 1):
    print(i) """
    
   #anzichè partire sempre da numero, mi dichiaro direttamente ripeti si
    
ripeti = "si"
    
while ripeti == "si":
    
    numero = int(input("Scrivi un nuovo numero: "))

    for i in range(0, numero + 1, 1):
        print(i)

    ripeti = input("Vuoi continuare? ")
    
    if ripeti != "si":
        print("Arrivederci")