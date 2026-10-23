import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv("CorsoPythonITConsulting/15_venerdi_23ottobre/TEST_VENERDI 23OTTOBRE/candy-data.csv")

print(df1.head()) #ho verificato i primi 5

print(df1.tail()) #verificato ultimi 5 

df1.info() #info relazione: questo dataset contiene 85 caramelle con 13 variabili diverse, info non mi segnala valori mancanti in queste colonne

print(df1.shape) #vediamo un po' le dimensioni

print(df1.isnull().sum()) #is null controlliamo tutte le celle e restituisce true se è mancante false se è pieno, infatti tutti 0 per ora, sum somma quelli che ci sono in ogni colonna

print(df1.duplicated().sum()) # cerchiamo doppioni

print(df1.describe())



df2 = pd.read_csv("CorsoPythonITConsulting/15_venerdi_23ottobre/TEST_VENERDI 23OTTOBRE/candy-vendite.csv")

print(df2.head()) #ho verificato i primi 5

print(df2.tail()) #verificato ultimi 5 

df2.info() #info relazione: questo dataset contiene 85 caramelle con 13 variabili diverse, info non mi segnala valori mancanti in queste colonne


print(df2.shape) #vediamo un po' le dimensioni

print(df2.isnull().sum()) #is null controlliamo tutte le celle e restituisce true se è mancante false se è pieno, infatti tutti 0 per ora, sum somma quelli che ci sono in ogni colonna

print(df2.duplicated().sum()) # cerchiamo doppioni

print(df2.describe()) #vediamoci anche un riepilogo statistico delle colonne


print("Caramelle nel primo CSV:", df1["competitorname"].nunique()) #nunique conta quanti nomi dicversi ci sono nella colonna competitor name
print("Caramelle nel secondo CSV:", df2["competitorname"].nunique())

print("Nomi presenti solo nel primo CSV:")
print(df1.loc[~df1["competitorname"].isin(df2["competitorname"]), "competitorname"]) #verifica se un valore è presente
#LOC indica che vogliamo selezionare qualcosa dalla tabella df1.
#e vediamo se è presente in competitor name di df2

print("Nomi presenti solo nel secondo CSV:")
print(df2.loc[~df2["competitorname"].isin(df1["competitorname"]), "competitorname"])


df_merge = pd.merge(df1,df2,on="competitorname", how="outer", indicator=True)
    #usa il nome della caramella come chiave di unione.
    #mantiene tutte le righe di entrambi i file.
    #aggiunge una colonna _merge che indica da quale file proviene ogni riga.

"""
colonna merge conterrà,
both: il nome è presente in entrambi i CSV
left_only: è presente soltanto in df1,
right_only: se è presente soltanto in df2

"""

print(df_merge.shape)
print(df_merge["_merge"].value_counts())

#Caramelle che hanno venduto di più 

top_vendite = df_merge.sort_values(by="unita_vendute",ascending=False)  # Ordina le righe del DataFrame
    # Usa le unità vendute come criterio (by da considerare spesso per fare questo tipo di operazioni)
       # Ordina dal valore più alto al più basso (grandioso, non lo conoscevo)

print(top_vendite[["competitorname", "unita_vendute"]].head(10))
    # Seleziona nome e unità vendute e mostra le prime 10 righe

# Caramelle che hanno venduto di meno

meno_vendute = df_merge.sort_values(by="unita_vendute", ascending=True)  # Ordina le righe del DataFrame
    # Usa le unità vendute come criterio
    # Ordina dal valore più basso al più alto


print(meno_vendute[["competitorname", "unita_vendute"]].head(10))
    # Seleziona nome e unità vendute e mostra le prime 10 righe


# Caramelle che hanno ricevuto le valutazioni più basse dagli utenti
meno_apprezzate = df_merge.sort_values(by="valutazione_clienti",ascending=True) # Ordina le righe del DataFrame  
# Usa il voto dei clienti come criterio e ordina dal voto più basso al più alto
print(meno_apprezzate[["competitorname", "valutazione_clienti"]].head(10)) 
 # Seleziona nome e valutazione e mostra le prime 10 righe
 
# Caramelle più vendute per area geografica

vendite_area = df_merge.sort_values(by="unita_vendute", ascending=False)
# Ordina le caramelle per unità vendute, dal valore più alto al più basso

print(vendite_area[["competitorname", "area_vendita", "unita_vendute"]].head(10))
# Seleziona nome, area geografica e unità vendute
# Mostra le prime 10 caramelle


#GRAFICI

# Grafico delle 10 caramelle più apprezzate

top_apprezzate = df_merge.sort_values(by="valutazione_clienti", ascending=False).head(10)
# Ordina per valutazione decrescente e seleziona le prime 10

plt.figure(figsize=(10, 6))  # Imposta le dimensioni del grafico
plt.bar(top_apprezzate["competitorname"], top_apprezzate["valutazione_clienti"])
# Crea un grafico a barre con nomi e valutazioni

plt.title("Le 10 caramelle più apprezzate")  # Aggiunge il titolo
plt.xlabel("Caramelle")  # Etichetta l'asse orizzontale
plt.ylabel("Valutazione clienti")  # Etichetta l'asse verticale
plt.xticks(rotation=45, ha="right")  # Inclina i nomi per renderli leggibili
plt.tight_layout()  # Sistema gli spazi del grafico
plt.show()  # Visualizza il grafico


# Grafico delle 10 caramelle più vendute

top_vendute = df_merge.sort_values(by="unita_vendute", ascending=False).head(10)
# Ordina per unità vendute, dal valore più alto al più basso

plt.figure(figsize=(10, 6))  # Imposta le dimensioni del grafico
plt.bar(top_vendute["competitorname"], top_vendute["unita_vendute"])
# Crea le barre delle unità vendute per ogni caramella

plt.title("Le 10 caramelle più vendute")  # Aggiunge il titolo
plt.xlabel("Caramelle")  # Etichetta l'asse orizzontale
plt.ylabel("Unità vendute")  # Etichetta l'asse verticale
plt.xticks(rotation=45, ha="right")  # Inclina i nomi
plt.tight_layout()  # Sistema gli spazi
plt.show()  # Visualizza il grafico


# Grafico delle 10 caramelle meno vendute

meno_vendute = df_merge.sort_values(by="unita_vendute", ascending=True).head(10)
# Ordina per unità vendute, dal valore più basso al più alto

plt.figure(figsize=(10, 6))  # Imposta le dimensioni del grafico
plt.bar(meno_vendute["competitorname"], meno_vendute["unita_vendute"])
# Crea le barre delle unità vendute

plt.title("Le 10 caramelle meno vendute")  # Aggiunge il titolo
plt.xlabel("Caramelle")  # Etichetta l'asse orizzontale
plt.ylabel("Unità vendute")  # Etichetta l'asse verticale
plt.xticks(rotation=45, ha="right")  # Inclina i nomi
plt.tight_layout()  # Sistema gli spazi
plt.show()  # Visualizza il grafico

# Grafico delle vendite totali per area geografica

vendite_per_area = df_merge.groupby("area_vendita")["unita_vendute"].sum()
# Raggruppa le righe per area e somma le unità vendute

plt.figure(figsize=(8, 5))  # Imposta le dimensioni del grafico
plt.bar(vendite_per_area.index, vendite_per_area.values)
# Usa le aree sull'asse orizzontale e le vendite totali su quello verticale

plt.title("Vendite totali per area geografica")  # Aggiunge il titolo
plt.xlabel("Area geografica")  # Etichetta l'asse orizzontale
plt.ylabel("Unità vendute")  # Etichetta l'asse verticale
plt.tight_layout()  # Sistema gli spazi
plt.show()  # Visualizza il grafico

"""nel quarto grafico usiamo groupby() e sum(): 
il primo raggruppa le caramelle per zona, il secondo somma le vendite di ogni gruppo. In questo modo non confondiamo la caramella
più venduta in assoluto con l'area che vende di più nel complesso."""