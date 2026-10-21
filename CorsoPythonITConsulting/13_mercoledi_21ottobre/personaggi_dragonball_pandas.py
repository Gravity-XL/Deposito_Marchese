

import pandas as pd

#lettura del file con path
df = pd.read_csv("CorsoPythonITConsulting/13_mercoledi_21ottobre/personaggi_dragonball.csv") 

print("Visualizziamo il tipo di dati")
print(df.info()) #visualizzo tutto il tipo di dati
print("")

print("Livello_Forza: Media, Mediana, Deviazione Standard")
print(df["livello_forza"].mean(), df["livello_forza"].median(),df["livello_forza"].std()) #ho fatto sia media, mediana e deciazione standard dell'età con la stampa
print("")

# stampa il valore massimo del livello forza
print("Livello forza più alto: ")
print(df["livello_forza"].max())
print("")

#creo guerrieri speciali, ed inserisco i guerrieri più forti di >= 7000, povero crilin
df["guerrieri speciali"] = df["livello_forza"] >= 7000
print(df)
print("")

#guerrieri più giovani, ed inserisco i guerrieri più giovani di <= 7000, povero crilin
df["guerrieri_giovani"] = df["eta"] <= 35
print(df)
print("")

"""index=False non elimina righe e non cancella l'indice dal DataFrame.
Dice soltanto a Pandas di non includere l'indice nel file salvato. Chiaramente
se fosse stato true l'avrebbe incluso"""

#ho cambiato il nome del file aggiungendo (_modifica) per non far sovrascrivere, e conservare una copia del precedente, così nel dubbio ho il file originale
df.to_csv("CorsoPythonITConsulting/13_mercoledi_21ottobre/personaggi_dragonball_modifica.csv", index=False)

print("Modifiche salvate nel file CSV!")




