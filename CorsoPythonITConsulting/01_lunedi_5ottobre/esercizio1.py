#valorizzazione delle variabili con i tipi


bool = bool(input("inserisci un bool "))
numint = int(input("inserisci un int "))
numfloat = float(input("inserisci un float "))
char = input ("inserisci un char ")
string = input("inserisci una parola ")

#stampa delle variabili
print(bool, " ", numfloat, " ", numint, " ", string, " ", char)

#inserimento dati numerici per effettuare la comparazione
numint1 = int(input("inserisci un int "))
numint2 = int(input("inserisci un int "))

#comparazione operatori logici
print(numint1 < numint2 and numint1 > numint2)
print(numint1 < numint2 or numint1 > numint2)
print(not(numint1 < numint2 and numint1 > numint2))