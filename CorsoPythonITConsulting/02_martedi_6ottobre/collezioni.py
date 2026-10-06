#LIST

numeri = [1,2,3,4,5]
nomi = ["Luca", "Mirko", "Marco"]
misto = [1, "due", True, 4.5] #con python posso aggiungere in una lista tipi diversi

print(numeri[0]) 
print(nomi[1])


numeri[3] = 8
print(numeri)

print(len(numeri)) #len_mi dice la lunghezza dei numeri, ti dice 5 perchè è per gli utenti

numeri.append(6) #append_aggiungi un elemento in lista
print(numeri) 

numeri.insert(2, 10) #alla posizione 2 aggiungi 10
print(numeri)


numeri.remove(8) #rimuove proprio il numero 4 (esempio cognome)
print(numeri) 

numeri.sort() #ordina i numeri
print(numeri)


