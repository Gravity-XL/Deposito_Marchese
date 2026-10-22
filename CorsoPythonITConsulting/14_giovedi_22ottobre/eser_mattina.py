""" Esercizio 1: Analisi di Vendite Fittizie
Obiettivo: Utilizzare pandas per analizzare un set di dati di vendite
generato casualmente, applicando le tecniche di pivot e groupby.
Descrizione: Gli studenti dovranno generare un DataFrame di vendite che
include i seguenti campi: "Data"
,
"Città"
,
"Prodotto" e "Vendite"
. I dati
devono essere generati per un periodo di un mese, con vendite registrate
per tre diverse città e tre tipi di prodotti.
1.Generazione dei Dati: Utilizzare numpy per creare un set di dati
casuali.
2.Creazione della Tabella Pivot: Creare una tabella pivot per analizzare
le vendite medie di ciascun prodotto per città.
3.Applicazione di GroupBy: Utilizzare il metodo groupby per calcolare le
vendite totali per ogni prodotto. """


import pandas as pd


#caricare i dati in un dataframe (fatto)
df = pd.read_csv("CorsoPythonITConsulting/14_giovedi_22ottobre/music.csv")

print(df)
print("")
df.head()	#Mostra le prime 5 righe
df.tail()	#Mostra le ultime 5 righe
df.info()	#Mostra colonne, tipi di dato e valori non nulli
df.describe()	#Fornisce statistiche descrittive sulle colonne numeriche
print("")

#nel pivot mi sono vatto vendite come colonna numerica,sulle righe l'index per il genere, colonna ho messo gli artisti e media valori
pivot_df = df.pivot_table(values="Vendite",index="Genere",columns="Artista", aggfunc="mean")
#ovviamente appariranno per generi diversi, quindi avremo delle colonne vuote
print("")
print(pivot_df)
print("")

#groupby, chiede le vendite totali per prodotto
#io mi gioco l'artista(come prodotto) per le vendite totali(gli album venduti)

groupby_df = df.groupby("Artista")["Vendite"].sum()
print("")
print(groupby_df)
print("")

