class Animale:

    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta

    def fai_suono(self):
        print(f"{self.nome} emette il suo verso.")


class Leone(Animale):

    def caccia(self):
        print(f"{self.nome} sta cacciando.")


class Giraffa(Animale):

    def mangia(self):
        print(f"{self.nome} sta mangiando.")


class Cane(Animale):

    def abbaia(self):
        print(f"{self.nome} sta abbaiando.")

        
 # CREAZIONE DEGLI OGGETTI

leone1 = Leone("Simba", 5)
giraffa1 = Giraffa("Melman", 8)
cane1 = Cane("Fido", 3)


# CHIAMATA DEI METODI SPECIFICI

leone1.caccia()
giraffa1.mangia()
cane1.abbaia()


# CHIAMATA DEL METODO EREDITATO

leone1.fai_suono()
giraffa1.fai_suono()
cane1.fai_suono()       