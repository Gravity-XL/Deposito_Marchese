class Libro:

    def __init__(self, titolo:str, autore:str, pagine:int):
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine

    def descrizione(self):
        return ("il libro ", {self.titolo}, " scritto da " ,{self.autore} ," ha " ,{self.pagine}, " pagine.")
    
    
titolo = input("Inserisci il titolo di un libro ")
autore = input("Inserisci l'autore del libro: ")
pagine = int(input("Inserisci il numero di pagine "))

libro1 = Libro(titolo, autore, pagine)

#inserire una distanza

libri = []

while True:
    
    titolo = input("Inserisci il titolo del libro: ")
    autore = input("Inserisci l'autore del libro: ")
    pagine = int(input("Inserisci il numero di pagine: "))

    libro = Libro(titolo, autore, pagine)
    libri.append(libro)

    continua = input("Vuoi inserire un altro libro? (si/no): ")

    if continua.lower() != "si":
        break
    
# come lha fatto mirko , base sul passs

class Libro:
    
    pass



scelta = ""

while scelta != "end":  
    
    pass  
