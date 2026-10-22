"""Esercizio: Analisi di un Centro Sportivo: iscritti, corsi e presenze
Gestisci i dati di un centro sportivo con:
1.Anagrafica iscritti
2.Registro presenze ai corsi
3.Tabella costi abbonamenti

Obiettivo
Pulire i dati, analizzare frequenze e costruire un report riepilogativo.
Dati da creare
1.DataFrame iscritti
a.Colonne: Nome, Eta, Citta, Tipo
_
Abbonamento (Base, Premium, Family)
b.Vincoli: almeno 10 righe, almeno 1 duplicato, almeno 1 valore mancante
2.DataFrame presenze
c.Colonne: Data, Corso (Yoga, Crossfit, Nuoto, Pilates), Citta, Partecipanti
d.Vincoli: almeno 15 righe, almeno 3 date, almeno 3 citta
3.DataFrame costi
abbonamento
_
e.Colonne: Tipo
_
Abbonamento, Costo Mensile"""


import pandas as pd

# Carico il CSV degli iscritti nel DataFrame
df_iscritti = pd.read_csv("CorsoPythonITConsulting/14_giovedi_22ottobre/iscritti.csv")

# Stampo gli iscritti originali
print(df_iscritti)

# Mostro le prime 5 righe per esplorare i dati
print(df_iscritti.head())

# Mostro informazioni su colonne e tipi di dato
df_iscritti.info()


# Carico il CSV delle presenze
df_presenze = pd.read_csv("CorsoPythonITConsulting/14_giovedi_22ottobre/presenze.csv")

# Ordino per città e poi per numero di partecipanti
df_presenze = df_presenze.sort_values(by=["Citta", "Partecipanti"])
print(df_presenze)

# Calcolo il totale dei partecipanti per ogni corso
totali_corso = df_presenze.groupby("Corso")["Partecipanti"].sum()
print(totali_corso)

# Calcolo la media dei partecipanti per città
media_citta = df_presenze.groupby("Citta")["Partecipanti"].mean()
print(media_citta)

# Creo una pivot table con i corsi sulle righe e le città sulle colonne
pivot_presenze = df_presenze.pivot_table(
    index="Corso",
    columns="Citta",
    values="Partecipanti",
    aggfunc="mean"
)
print(pivot_presenze)

# Creo un nuovo DataFrame con sede, anno e numero di iscritti
df_sedi = pd.DataFrame({
    "Sede": ["Nord", "Nord", "Centro", "Centro", "Sud", "Sud"],
    "Anno": [2024, 2025, 2024, 2025, 2024, 2025],
    "Iscritti": [120, 135, 95, 110, 80, 105]
})

# Imposto Sede e Anno come indici multilivello
df_sedi = df_sedi.set_index(["Sede", "Anno"])
print(df_sedi)

# Seleziono tutte le righe della sede Nord
print(df_sedi.loc["Nord"])

# Seleziono il numero di iscritti della sede Centro nel 2025
print(df_sedi.loc[("Centro", 2025), "Iscritti"])


#da ricontrollare e finire, non l'ho completato