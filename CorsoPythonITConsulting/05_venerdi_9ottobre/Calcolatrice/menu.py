import utility as ty

a = int(input("inserisci un numero: "))

print("1. Somma")
print("2. Sottrazione")
print("3. Moltiplicazione")
print("4. Divisione")
4
operazione = input("Scegli un'operazione: ")

b = int(input("Inserisci il secondo numero: "))

if operazione == "1":
    risultato = ty.somma(a, b)
    print("Risultato:", risultato)

elif operazione == "2":
    risultato = ty.sottrai(a, b)
    print("Risultato:", risultato)

elif operazione == "3":
    risultato = ty.moltiplica(a, b)
    print("Risultato:", risultato)

elif operazione == "4":
    risultato = ty.dividi(a, b)
    print("Risultato:", risultato)

else:
    print("Operazione non valida!")
    
    #volendo posso aggiungere "scelta non valida se si inserisce un chat anzichè int"