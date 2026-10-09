numero = int(input("Inserisci un numero positivo: "))

while numero <= 0:  
    print("Numero non valido, inserisci un nuovo numero.")
    numero = int(input("Inserisci un numero positivo: "))


# Somma dei numeri pari

somma = 0

print("Numeri pari: ")

for i in range(1, numero + 1):
    if i % 2 == 0:
       # print(i) capire se dovevo stampare o meno tutti i numeri
        somma = somma + i

print("La somma dei numeri pari è: ", somma)


# Numeri dispari da elencare e stampare ma senza la somma
print("Numeri dispari: ")

for i in range(1, numero + 1):
    if i % 2 != 0:
        print(i)


# Verifica se il numero è primo, con molta difficoltà mi sono aiutato con internet ma dopo che l'ho cercato l'ho capito
primo = True

if numero == 1:
    primo = False
else:
    for i in range(2, numero):
        if numero % i == 0:
            primo = False
            break

if primo:
    print("Il numero è primo")
else:
    print("Il numero non è primo")