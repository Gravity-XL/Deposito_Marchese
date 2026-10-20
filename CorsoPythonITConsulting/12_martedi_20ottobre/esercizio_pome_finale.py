#parte 1, 2-3 extra 

"""Parte 1:
Scrivere un Sistema che utilizza NumPy per gestire una matrice 2D.
Il programma deve presentare un menu interattivo che consente all'utente di eseguire varie operazioni
sulla matrice. Le operazioni disponibili includono, ogni volta che il sistema conclude un calcolo va
salvato su un file txt:
1.Creare una nuova matrice 2D di dimensioni specificate da utente con numeri casuali.
2.Estrarre e stampare la sotto-matrice centrale.
3.Trasporre la matrice e stamparla.
4.Calcolare e stampare la somma di tutti gli elementi della matrice.
5.Uscire dal programma o ripetere.

PARTE BASE

Parte 2:
Andare a specializzare per aggiungere nuove operazioni:
1.Moltiplicazione Element-wise con un'altra Matrice: L'utente può scegliere di creare una seconda matrice
delle stesse dimensioni della prima e moltiplicarle elemento per elemento e stampare il risultato.
2.Calcolo della Media degli Elementi della Matrice: Calcolare e stampare la media di tutti gli elementi
della matrice.
EXTRA:
Determinante della Matrice: Calcolare e stampare il determinante della matrice (solo se la matrice è
quadrata es. 2x2, 3x3, 4x4)."""


#extra 244

#mi faccio prima le operazioni e successivamente penserò al menu

import numpy as np

#QUESTO ESERCIZIO MI SERVE PER L'UTILITY PER COPIARMI TUTTE QUESTE OPERAZIONI E SOSTITUIRE 
#VELOCEMENTE I VALORI CHE MI SERVONO

#preferisco lavorare con la funzione def almeno posso richiamarmelo successivamene
def crea_matrice():
    righe = int(input("Quante righe vuoi? "))  #chiedo all'utente righe e colonne
    colonne = int(input("Quante colonne vuoi? "))

    matrice = np.random.randint(1, 101, size=(righe, colonne)) #creiamo la matrice con i numeri (riguardato esempio esercizio precedente)

    print("Matrice creata:\n", matrice) # printo la matrice


    #DA RIPETERE ed inserire assolitamente nel file utility finale che ho deciso di costruire per ogni passaggio che voglio
    with open("CorsoPythonITConsulting/12_martedi_20ottobre/risultati.txt", "a") as file:
        file.write("Matrice creata:\n" + str(matrice) + "\n")  #open copiato e incollato, sintassi a me quasi sconosciuta praticamente

    return matrice

matrice = crea_matrice() #esegue la funzione e salva la matrice restituita nella variab matrice

#sottomatrice l'ho fatta tenendo conto di un 4x4 come dicevamo per non avere problemi
#e senza fare quindi la parte di oggi dimensioni leading come dicevi a malek
#e quindi andare comodi per una sottomatrice 2x2

def estrai_sottomatrice(matrice):
    sotto_matrice = matrice[1:3, 1:3]

    print("Sottomatrice centrale:\n", sotto_matrice)

    #str(sotto_matrice) così stampiamo in testo dentro il file
    with open("CorsoPythonITConsulting/12_martedi_20ottobre/risultati.txt", "a") as file:
        file.write("Sottomatrice centrale:\n" + str(sotto_matrice) + "\n") 
        
        

    return sotto_matrice #visto che avevo il txt ci ho riflettuto sul return, ma abbiamo un menu da fare
#quindi magari può tornarci utile quel return per ritornarci la sottomatrice

estrai_sottomatrice(matrice) #così me la richiamo per provarla


#mi sono ricopiato esattamente lo stesso metodo di sopra ma l'ho fatto con il trasponi matrice


def trasponi_matrice(matrice):
    matrice_trasposta = matrice.T #questo matrice.T che non abbiamo mai visto forse era uno
    #dei metodi che diceva mirko per poter automatizzare la trasposizione e cioè scambiare righe e colonne.

    print("Matrice trasposta:\n", matrice_trasposta)

    with open("CorsoPythonITConsulting/12_martedi_20ottobre/risultati.txt", "a") as file:
        file.write("Matrice trasposta:\n" + str(matrice_trasposta) + "\n")

    return matrice_trasposta

trasponi_matrice(matrice) #così me la richiamo per provarla

#stessa cosa qui, metodo somma per il menu e ci metto il sum, leggi i commenti sopra, è uguale

def somma_matrice(matrice):
    somma = np.sum(matrice)

    print("Somma di tutti gli elementi:", somma)

    with open("CorsoPythonITConsulting/12_martedi_20ottobre/risultati.txt", "a") as file:
        file.write("Somma di tutti gli elementi: " + str(somma) + "\n")

    return somma

somma_matrice(matrice)


#uscire dal programma o ripetere (cioè l'ultimo punto del menu, lo rimando a dopo)

#MOLTIPLICA MATRICI è LEGGERMENTE DIVERSO
#facciamo il metodo ma con size = matrice.shape prendo la "forma" della prima matrice e lo butto nel size della seconda
#da notare "butto" gergo informatico.


def moltiplica_matrici(matrice):
    seconda_matrice = np.random.randint(1, 101, size=matrice.shape) #size matrice

    print("Seconda matrice:\n", seconda_matrice)

    risultato = matrice * seconda_matrice #facciamo la variabile risultato per richiamarcelo dopo

    print("Risultato della moltiplicazione:\n", risultato)


    #mi riporto nel file di testo sia la matrice in stringa che il risultato in stringa
    with open("CorsoPythonITConsulting/12_martedi_20ottobre/risultati.txt", "a") as file:
        file.write("Seconda matrice:\n" + str(seconda_matrice) + "\n")
        file.write("Moltiplicazione element-wise:\n" + str(risultato) + "\n")

    return risultato

  #IDENTICO A SOMMA MA HO USATO IL MEAN, il resto è esattamente uguale, ma tutto con la media quindi
def media_matrice(matrice):
    media = np.mean(matrice)

    print("Media degli elementi:", media)

    with open("CorsoPythonITConsulting/12_martedi_20ottobre/risultati.txt", "a") as file:
        file.write("Media degli elementi: " + str(media) + "\n")

    return media

#per il determinante NON FINITO, mi sono solo copiato il linalg:

determinante = np.linalg.det(matrice) #su una matrice di 2x2, 4x4 ecc 
#quindi quadrata il determinante è il risultato della moltiplicazione dei diagonali
#e sottrarli 