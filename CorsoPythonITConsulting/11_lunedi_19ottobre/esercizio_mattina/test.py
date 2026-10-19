

Test_file = open("CorsoPythonITConsulting/11_lunedi_19ottobre/esercizio_mattina/test_file.txt")

#contenuto_file_riga = Test_file.readline()
#print(contenuto_file_riga)

while True:
    print("\n--- GESTIONE FILE ---")
    print("1. Crea un file")
    print("2. Modifica un file")
    print("3. Leggi un file")
    print("4. Svuota un file")
    print("5. Esci")

    scelta = input("Scegli un'opzione: ")

    match scelta:
        case "1":
            
            Test_file = open("CorsoPythonITConsulting/11_lunedi_19ottobre/esercizio_mattina/test_file.txt", "w")
            Test_file.write(" Ora esisto ")
            Test_file.close()
            
            
            print("Crea un file")

        case "2":       
            Test_file = open("CorsoPythonITConsulting/11_lunedi_19ottobre/esercizio_mattina/test_file.txt", "a")
            Test_file.write(", ti ho appena aggiunto con append ")
            Test_file.close()
            
            
            print("Modifica un file")

        case "3":
            Test_file = open("CorsoPythonITConsulting/11_lunedi_19ottobre/esercizio_mattina/test_file.txt", "r")
            Test_file.read()
            #contenuto = file.read() da rivedere per la lettura
            Test_file.close()
            
            
            
            print("Leggi un file")

        case "4":
            print("Svuota un file")
            Test_file = open("CorsoPythonITConsulting/11_lunedi_19ottobre/esercizio_mattina/test_file.txt", "w")
            Test_file.write()
            Test_file.close()

        case "5":
            print("Programma terminato!")
            break

        case _:
            print("Scelta non valida!")