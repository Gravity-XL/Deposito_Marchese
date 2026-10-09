n = int(input("Inserisci un numero positivo: "))

while n <= 0:
    n = int(input("Non è positivo, inserisci un numero positivo: "))
    
# lista = [] non ha senso che mi scrivo una lista vuota se dopo la riscrivo con cosa deve riempirsi, posso farla direttamente     
    
import random

lista = [random.randint(1, n) for _ in range(n)] #lista già con il random, mi sono aiutato con internet e l'underscore dovrebbe esserebe essere un valore per continuare senza assegnare , DA RICONTROLLARE
print (lista)


#punto3


somma = 0 #mi chiamo la variabile somma

for i in lista: #for per i pari
    if i % 2 == 0:
        somma = somma + i

print(somma)

#punto4

for i in lista: #for per i dispari
    if i % 2 != 0:
        print(i)
        
#punto 5

def pari(numero): #utilizzo direttamente return, ragionavo se usare un ciclo, ma fondamentalmente ciò che voglio è true o false, quindi posso ottenerlo così
    return numero % 2 == 0
if pari(n):
    print("Il numero è pari")
else:
    print("Il numero è dispari")
        
        
#punto 6

for numero in lista:  #utilizzo il ciclo per stampare tutti i numeri pari
    if pari(numero):
        print(numero)
        
#punto 7 DA RICONTROLLARE 

if somma % 2 == 0:
    print("La somma è pari")
else:
    print("La somma è dispari")