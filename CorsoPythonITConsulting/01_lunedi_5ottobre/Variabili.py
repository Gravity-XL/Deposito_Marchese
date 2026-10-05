#Test variabili e tipi di variabile

nome_variabile = "stringa"
numero = 1

#testo sull'indicizzazione
s = "test"
print(s[2])
print(s[3])


#concatenazione + input utente
saluto = input("Inseriscimi un saluto ")
nome = input("Inserisci il tuo nome ")
messaggio = saluto + " " + nome
print(messaggio)

#prova di alcune funzioni

s= "Ciao, mondo"
print(len(s))
print(s.upper())
print(s.split(","))
print(s.replace("mondo" , "universo")) 

#testo booleani

x = 2
y = 3
z = 5

print (x==y)
print (x != y)


print (x < y or x > y)
print(x < y or z > y)


