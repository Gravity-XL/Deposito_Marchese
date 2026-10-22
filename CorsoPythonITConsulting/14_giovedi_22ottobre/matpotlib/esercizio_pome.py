#facciamo un grafico spotify che registra gli ascolti giornalieri di un artista
#poi ci dice ascolto massimo, minimo, medio e la mediana degli ascolti

import pandas as pd
import matplotlib.pyplot as plt

df_ascolti = pd.read_csv("CorsoPythonITConsulting/14_giovedi_22ottobre/matpotlib/ascolti_artist.csv")


#TOTALE DEGLI ASCOLTI STAMPATI
print("____ASCOLTI ANN0____")
print(df_ascolti)

print("")

#ASCOLTO MASSIMO
ascolto_massimo = df_ascolti["Ascolti"].max()
print("ASCOLTO MASSIMO:", ascolto_massimo)

print("")

#ASCOLTO MINIMO
ascolto_minimo = df_ascolti["Ascolti"].min()
print("ASCOLTO MINIMO:", ascolto_minimo)

print("")

#ASCOLTO MEDIO
ascolto_medio = df_ascolti["Ascolti"].mean()
print("ASCOLTO MEDIO:", ascolto_medio)

print("")

#ASCOLTO MEDIAMO
ascolto_mediano = df_ascolti["Ascolti"].median()
print("ASCOLTO MEDIANO:", ascolto_mediano)

print("")

#ho scelto il grafico a barre ed ho richiamato come abbiamo fatto nell'esempio tutti i valori all'interno
#del grafico


print("GRAFICO A BARRE")

categories = df_ascolti["Mese"]
values = df_ascolti["Ascolti"]

plt.figure()
plt.bar(categories, values)
plt.title("Ascolti su Spotify")
plt.xlabel('Mesi')
plt.ylabel('Ascolti')
plt.show() 
