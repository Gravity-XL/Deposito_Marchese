"""L'obiettivo di questo esercizio è generare un set di dati analizzarli con pandas e visualizzare i risultati usando Matplotlib. Gli studenti dovranno eseguire le seguenti operazioni:

1. Generazione dei Dati: Utilizzare NumPy per generare una serie temporale di 365 giorni di dati, simulando il numero di visitatori giornalieri in un parco, assumendo che il numero medio di visitatori sia 2000 con una deviazione di 500.

2. Creazione del DataFrame: Creare un DataFrame pandas o caricarlo con le date come indice e il numero di visitatori come colonna.

3. Analisi dei Dati: Calcolare il numero medio di visitatori per mese e la deviazione standard.

4. Visualizzazione dei Dati:
- Creare un grafico a linee del numero di visitatori giornalieri.
- Esplorativa: Aggiungere al grafico la media mobile a 7 giorni per mostrare la tendenza settimanale.
- Creare un secondo grafico che mostri la media mensile dei visitatori."""


#Ho riprodotto l'esercizio con uno scenario simile ma in un contesto completamente diverso

#Monitoraggio della qualità microbiologica dell'acqua, ho fatto il grafico della concentrazione giornaliera e il grafico della concentrazione media mensile


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Genero 365 misurazioni giornaliere della concentrazione batterica nell'acqua

#prendo il csv

df_monitoraggio_acqua = pd.read_csv("CorsoPythonITConsulting/14_giovedi_22ottobre/matpotlib/monitoraggio_qualita_acqua.csv")

# Stampo le prime 5righe del DataFrame giusto per fare un check velce
print(df_monitoraggio_acqua.head())

# Calcolo e stampo la media e la deviazione standard
print("Concentrazione batterica: Media e Deviazione Standard")
print(df_monitoraggio_acqua["Concentrazione_batterica_UFC_100mL"].mean(),
      df_monitoraggio_acqua["Concentrazione_batterica_UFC_100mL"].std())
print("")

# Converto la colonna Data da testo a formato data visto che ho scoperto che se le caricavo 2026-01-01 lo fa come test e non come date
#quindi ho trovato questo to_datetime, ottimo per fare le date da un testo
df_monitoraggio_acqua["Data"] = pd.to_datetime(df_monitoraggio_acqua["Data"])

# Imposto la colonna Data come indice per poter raggruppare le misurazioni per mese dopo averlo trasformato in data
df_monitoraggio_acqua = df_monitoraggio_acqua.set_index("Data")

# Calcolo la concentrazione batterica media per ogni mese
#resample() serve a raggruppare i dati in intervalli di tempo, per esempio per giorno
# mese o anno, quando le date sono impostate come indice del DataFrame. 
media_mensile = df_monitoraggio_acqua["Concentrazione_batterica_UFC_100mL"].resample("ME").mean()

# Stampo la media delle concentrazioni batteriche per ciascun mese
print("Concentrazione batterica media mensile:")
print(media_mensile)
print("")


# Calcolo la media mobile su 7 giorni consecutivi delle concentrazioni batteriche, ci devo riflettere un secondo!
media_mobile = df_monitoraggio_acqua["Concentrazione_batterica_UFC_100mL"].rolling(window=7).mean()

# Stampo i valori della media mobile a 7 giorni
print("Media mobile a 7 giorni:")
print(media_mobile)
print("")

# Creo il grafico lineare delle concentrazioni batteriche rilevate ogni giorno
plt.figure(figsize=(12, 5))
plt.plot(df_monitoraggio_acqua.index, df_monitoraggio_acqua["Concentrazione_batterica_UFC_100mL"])

# Aggiungo il titolo e le etichette degli assi
plt.title("Concentrazione batterica giornaliera nell'acqua")
plt.xlabel("Data")
plt.ylabel("Concentrazione batterica (UFC/100 mL)")

# Ruoto le date per renderle più leggibili
plt.xticks(rotation=45)

# Adatto gli spazi e mostro il grafico
plt.tight_layout()
plt.show()


# Creo il grafico lineare delle concentrazioni batteriche medie mensili
plt.figure(figsize=(10, 5))
plt.plot(media_mensile.index, media_mensile.values, marker="o")

# Aggiungo il titolo e le etichette degli assi
plt.title("Concentrazione batterica media mensile nell'acqua")
plt.xlabel("Mese")
plt.ylabel("Concentrazione media (UFC/100 mL)")

# Ruoto le date per renderle più leggibili
plt.xticks(rotation=45)

# Adatto gli spazi e mostro il grafico
plt.tight_layout()
plt.show()





