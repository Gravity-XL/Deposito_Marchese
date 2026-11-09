# Esercizio Omnicomprensivo


# PUNTO 1_ DEFINIZIONE DEL PROBLEMA
# 
# il punto uno ci chiede di apprendere il tipo di problema, essendo 0 e 1, è un problema 
# di classificazione, è supervisionato perchè conosciamo l'output, 
# la colonna target è appunto maligno o benigno, cioè 0 e 1, a noi interessa trovare 0.


from sklearn.datasets import load_breast_cancer

cancer = load_breast_cancer(as_frame=True)
#print(cancer)


# 2 stampo forma di X e y
X = cancer.data
y = cancer.target

print("Forma di X (Features):", X.shape)
print("Forma di y (Target):", y.shape)

#stampo nomi delle future e delle classi

print(cancer.feature_names)
print(cancer.target_names)

#stampo le prime 5 righe di codice

print(cancer.frame.head())

#stampa il contenuto di DESCR

print(cancer.DESCR)

#controllo campioni per classe con "value_counts"

print(y.value_counts())

#minimo e massimo di tutte le feature , saranno importanti più avanti 
#con loc mi seleziono ciò che voglio

riepilogo = X.describe().loc[["min", "max", "std"]].T

# Ordino le feature in base al valore massimo, dal più alto al più basso,
# e stampo tutta la tabella senza abbreviazioni.
print(riepilogo.sort_values(by="max", ascending=False).to_string())

#commento: serve per il nostro K,

# OSSERVAZIONE DELLE SCALE DELLE FEATURES

# Confronto due features con scale numeriche molto diverse.

print("\nWorst area:")
print("Min:", X["worst area"].min())
print("Max:", X["worst area"].max())

print("\nWorst fractal dimension:")
print("Min:", X["worst fractal dimension"].min())
print("Max:", X["worst fractal dimension"].max())

# Le features hanno scale numeriche molto diverse.
# Questo può influenzare KNN, perché il modello calcola le distanze
# tra i campioni e le features con valori più grandi possono incidere maggiormente.
# Successivamente utilizzeremo lo scaling per rendere confrontabili le scale.


#da finire con calma, c'è la correzione anche su git