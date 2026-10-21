

import pandas as pd


# Creazione di un DataFrame con dati di esempio
data = {
'Nome': ['Alice', 'Bob', 'Carla'],
'Età': [25, 30, 22],
'Città': ['Roma', 'Milano', 'Napoli']
}

# aggiunta di una chiave al dizionario
data["Sesso"] = ["F","M","F"]
data["Exp"] = ["120", "35", "71"]

df = pd.DataFrame(data)

#stampa del DataFrame originale
#print("")


print(df.head()) #se non metto niente nella parentesi, mi stampa di base le prime 5 #print(df.head(1))
print(df.tail()) #se non metto niente nella parentesi, mi stampa di base le prime 5
print(df.describe()) #tutte le info numeriche che abbiamo
print(df.info()) #riporta ogni informazione, ogni colonna, il tipo di dato e se ho valori, se ho null o non-null (nessun errore)

#RICORDA IL NULL NON TI DICE SE è NULL NEL CASO CI FOSSE, MA TI SCALA 1 ELEMENTO, SE TUTTI NE HANNO 3 ED UNO 2, MAGARI MANA IL TERZO PERCHè è
#SBAGLIATO O è APPUNTO NULL


#CSV= df_scv = pd.read_csv

#di età ad esempio

#count = numero di età che abbiamo"
#mean = la media
#std = la deviazione
#min = minimo dell'età
#25% = in che percentuale
#50% = in che percentuale
#75% = in che percentuale
#max = età massima
 
df_scv = pd.read_csv("CorsoPythonITConsulting/13_mercoledi_21ottobre/studenti.csv")

print(df_scv)

#df_scv["sesso"] = [] #nuova colonna

print(df_scv)

#crea una colonna promosso riempendola di valori booleani in base alla condizione, (broadcasting)

df_scv["promosso"] = df_scv["voto"] >= 6

print(df_scv)

#stampa la media dei voti_SONO UNIVERSALI, NON MODIFICANO I RISULTATI FINALI
print(df_scv["voto"].mean())
print("")

#stampa il valore massimo dei voti_SONO VALORI UNIVERSALI, NON MODIFICANO I RISULTATI FINALI
print(df_scv["voto"].max())
print("")

#stampa di una condizione booleana_LINEARE NON UNIVERSALE, PERCHè RIPORTA UN VALORE SOLO
print(df_scv[df_scv["voto"] > 7])
print("")

#salva il DataFrame in un nuovo CSV, mi ha creato studenti_aggiornato
df_scv.to_csv("CorsoPythonITConsulting/13_mercoledi_21ottobre/studenti_aggiornato.csv", index = False)