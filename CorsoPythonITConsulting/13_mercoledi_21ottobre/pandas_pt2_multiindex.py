

#MULTIINDEX

import pandas as pd

"""MultiIndex è un indice "a più livelli" in Pandas: invece di identificare una riga con una sola
chiave, usi una combinazione di chiavi (es. Paese + Anno).
Serve quando i dati hanno una struttura gerarchica, perché rende più naturale filtrare e
organizzare informazioni per gruppi combinati."""


data_multi = {
    'Paese': ['Italia', 'Italia', 'Francia', 'Francia'],
    'Anno': [2023, 2024, 2023, 2024],
    'Vendite': [120, 135, 110, 118]
}

df_multi = pd.DataFrame(data_multi)

# Creo un indice gerarchico con Paese e Anno
df_multi = df_multi.set_index(['Paese', 'Anno'])

print("\nDataFrame con MultiIndex:")
print(df_multi)


print("-----------------------------")


#LOC - SELEZIONE PER VALORE, lavora sui valori e non la chiave, esempio genere rap


"""Esempio Pratico: Loc
loc è il selettore basato su etichette (nomi), non su posizione numerica:
seleziona righe/colonne per nome con MultiIndex puoi selezionare un livello o una
combinazione di livelli.
è utile per query leggibili e precise"""


#da copiare loc



#PIVOT

import pandas as pd

# Dati di esempio
data = {
'Data': ['2021-01-01', '2021-01-01', '2021-01-01', '2021-01-02', '2021-01-02'],
'Città': ['Roma', 'Milano', 'Napoli', 'Roma', 'Milano'],
'Prodotto': ['Mouse', 'Tastiera', 'Mouse', 'Tastiera', 'Mouse'],
'Vendite': [100, 200, 150, 300, 250]
}

df = pd.DataFrame(data)

#abbiamo fatto l'esempio che a napoli corrisponde solo mouse, quindi esce NaN, mentre se aggiungessimo
#anche la tastiera chiaramente lo riporterebbe

# Creazione della tabella pivot
pivot_df = df.pivot_table(values='Vendite', index='Prodotto', columns='Città', aggfunc='mean')

print(pivot_df)
