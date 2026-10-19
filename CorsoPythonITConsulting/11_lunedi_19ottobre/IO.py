




File_valorizzato_da_open = open("CorsoPythonITConsulting/11_lunedi_19ottobre/luca.txt", "r")

#metodo di lettura line by line del file
contenuto_file_riga = File_valorizzato_da_open.readline()
print(contenuto_file_riga)

#metodo di lettura totale del file
contenuto_file_totale = File_valorizzato_da_open.read()
print(contenuto_file_totale)


#il risultante dalla lettura è una sorta di oggetto

File_valorizzato_da_open.close()

File_valorizzato_da_open = open("CorsoPythonITConsulting/11_lunedi_19ottobre/luca.txt", "w")
File_valorizzato_da_open.write("Eccomi caro")

File_valorizzato_da_open.close()

#il drive se non esiste il file LO CREA, se esiste LO SOVRASCRIVE, tipo modifica gioco
#il close disimpegna la ram, 

#il with avanti all'open fa automaticamente il close, va fatta dopo aver comunque caricato il path

#open deriva dal sistema operativo, la sfrutta python ma esiste già
#slide 195 tutte le modalità

# w crea il file, o modifica quello esistente
# w potrei anche svuolare tutto mettendo, write vuoto
# r,w,a,x (i più importanti)




