from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Per prima cosa carico il dataset Wine, che contiene le caratteristiche
# chimiche dei vini e la classe di appartenenza di ogni campione.
wine = load_wine()

# Separo le caratteristiche dalla classe che voglio prevedere.
# X contiene i dati chimici dei vini, mentre y contiene le classi.
X = wine.data
y = wine.target

# Divido i dati in due gruppi: il 75% servirà per addestrare il modello,
# mentre il 25% servirà per verificare come si comporta su dati non usati
# durante l'addestramento. Uso random_state=0 per rendere la divisione
# riproducibile, cioè ottenere la stessa divisione a ogni esecuzione.
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=0
)

# Creo una lista con i due criteri che voglio confrontare.
# Gini ed Entropy misurano entrambi l'impurità dei gruppi, ma con formule
# diverse. L'albero li utilizza per scegliere come dividere i dati.
criteri = ["gini", "entropy"]

# Preparo una lista vuota nella quale raccolgo i risultati di tutti
# i modelli, così alla fine potrò confrontarli in una tabella.
risultati = []

# Inizio il primo ciclo: provo prima Gini e poi Entropy.
for criterio in criteri:

    # Per ogni criterio provo sei profondità diverse, da 1 a 6.
    # max_depth limita il numero di livelli decisionali dell'albero.
    for profondita in range(1, 7):

        # Creo l'albero con il criterio e la profondità attuali.
        # random_state=0 rende riproducibile il modello.
        albero = DecisionTreeClassifier(
            criterion=criterio,
            max_depth=profondita,
            random_state=0
        )

        # Addestro il modello usando solamente i dati di training.
        albero.fit(X_train, y_train)

        # Calcolo le previsioni sui dati di training per capire
        # quanto bene il modello classifica i dati che ha già visto.
        pred_train = albero.predict(X_train)

        # Calcolo le previsioni sui dati di test per verificare
        # come il modello si comporta su dati non usati per imparare.
        pred_test = albero.predict(X_test)

        # Calcolo l'accuratezza confrontando le previsioni con
        # le classi reali, sia per il training sia per il test.
        acc_train = accuracy_score(y_train, pred_train)
        acc_test = accuracy_score(y_test, pred_test)

        # Salvo il criterio, la profondità e le due accuratezze.
        # Arrotondo i valori a tre cifre decimali per leggerli meglio.
        risultati.append([
            criterio,
            profondita,
            round(acc_train, 3),
            round(acc_test, 3)
        ])

# Stampo una tabella con i risultati di tutti e dodici i modelli.
print("Criterio | Profondità | Accuracy training | Accuracy test")
for risultato in risultati:
    print(
        risultato[0], "|",
        risultato[1], "|",
        risultato[2], "|",
        risultato[3]
    )

# Cerco la combinazione con l'accuratezza di test più alta.
# Uso la colonna 3 di ogni riga, che contiene l'accuracy di test.
migliore = max(risultati, key=lambda r: r[3])

# Stampo il criterio, la profondità e l'accuratezza di test
# della combinazione che ha ottenuto il risultato migliore.
print("\nCombinazione migliore:")
print("Criterio:", migliore[0])
print("Profondità:", migliore[1])
print("Accuracy test:", migliore[3])
