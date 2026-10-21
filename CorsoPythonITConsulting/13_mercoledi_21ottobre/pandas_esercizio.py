#ho creato il dataframe

import pandas as pd

df = pd.read_csv("CorsoPythonITConsulting/13_mercoledi_21ottobre/esempio_dataset.csv") 
#leggo il file con il path

print("")
print("Prime 5 righe:")
print(df.head(5)) #visualizzo le prime 5 righe
print("")
print("Uiltime 5 righe")
print(df.tail(5)) #visualizzo le ultime 5 righe
print("")
print("Visualizziamo il tipo di dati")
print(df.info()) #visualizzo tutto il tipo di dati
print("")
print("ETA: Media, Mediana, Deviazione Standard")
print(df["eta"].mean(), df["eta"].median(),df["eta"].std()) #ho fatto sia media, mediana e deciazione standard dell'età con la stampa
print("")
print("SALARIO: Media, Mediana, Deviazione Standard")
print(df["salario"].mean(), df["salario"].median(),df["salario"].std()) #ho fatto sia media, mediana e deciazione standard del salario con la stampa
print("")
print("RIMUOVO EVENTUALI DUPLICATI")
df = df.drop_duplicates() #print dopo aver rimosso i duplicati (mi ero messo 2 volte, luca 34 ecc per provarlo
print(df) 
print("")
# possiamo sostituire dati mancanti con valore di default, ho un problema di visualizzazione, da riguardare
print("Gestione valori mancanti")
df['salario'].fillna(df['salario'].median(), inplace=True) # old versions
print(df)
print("")


