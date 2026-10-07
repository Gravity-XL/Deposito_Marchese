""" esercizio1:



Ciclo while: Descrizione: scrivi un programma che chiede all'utente 
di inserire numeri interi fino a quanto l'utente inserisce il numero 0. quando viene inserito 0 
il programma deve calcolare e stampare la somma di tutti i numeri inseriti. """


numeri = []

while True:
    
 
    numero = int(input("Scrivi un numero: "))
    
    if numero != 0:
     numeri.append(numero)
    else:
        break
  
  
    somma = 0
    
    for numero in numeri:
        somma = somma + numero
        
        
print(somma)
        
#-----------------------------------------

    """ esercizio 2 ciclo for :descrizione:
    scrivi un programma che chieda all'utente di inserire una parola e poi utilizzi 
    un ciclo for per stampare ogni lettera della parola su una nuova riga
    
    """
    
    parola = input("Inserisci una parola")
    
    for lettera in parola:
        print(char)
        
        