


import pandas as pd

#Volevo realizzare una tabella che tenesse traccia di vendite, anni, generi e artisti, e analizzare un po' di dati
#come i generi che hanno venduto di più, artisti ecc. insomma divertirmi a far uscire fuori dei dati in base a quello che mi interessava
#infatti farlo con dati scelti da noi, ti aiuta a capire come poter ragionare sulle informazioni che vogliamo.


#caricare i dati in un dataframe (fatto)
df = pd.read_csv("CorsoPythonITConsulting/13_mercoledi_21ottobre/music.csv")

print(df)


print("----------------TABELLA CON ARTISTI, ANNO, COLONNE-----------------")

#la traccia dice aggiungi una colonna "totale vendite" che sia il risultato del prodotto tra quantità e prezzo unitario
#noi potremmo fare (vendite, artista, anno e sum) 

# Creazione della tabella pivot
pivot_df = df.pivot_table(values="Vendite", index="Artista", columns="Anno", aggfunc="sum")

print(pivot_df)
print("")

#values="Vendite": mostra i numeri delle vendite.
#index="Artista": mette gli artisti sulle righe.
#columns="Anno": mette gli anni sulle colonne.
#aggfunc="sum": somma le vendite se ci sono più righe per lo stesso artista e anno.
print("")
print("---------------- VENDITE DIVISE PER GENERI -----------------")
print("")
#osserviamo le vendite totali per i generi, quindi prendiamo genere e vendite come i valori del groupby

# Raggruppo le vendite per genere e le sommo
vendite_genere = df.groupby("Genere")["Vendite"].sum()

print(vendite_genere)

print("")
print("---------------- GENERE CHE HA VENDUTO DI PIU -----------------")
print("")
# Trovo il genere che ha venduto di più, che poi paragonato alla traccia potrebbe essere la città
genere_top = vendite_genere.idxmax()
print("")
print("Il genere che ha venduto di più è:", genere_top)

print("Vendite totali:", vendite_genere.max(), "milioni di copie")

print("")
print("---------------- VENDITE ARTISTA TOTALI -----------------")
print("")
#osserviamo le vendite totali degli artisti, quindi prendiamo artista e vendite come i valori del groupby

# Raggruppo le vendite per artista
vendite_artista = df.groupby("Artista")["Vendite"].sum()

print(vendite_artista)

print("")
print("---------------- L'ARTISTA CHE HA VENDUTO DI PIU E' -----------------")
print("")

# Trovo l'artista che ha venduto di più
artista_top = vendite_artista.idxmax()
print("")
print("l'artista che ha venduto di più è:", artista_top, "con", vendite_artista.max(), "milioni di copie")

#print("Vendite totali:", vendite_genere.max(), "milioni di copie")


