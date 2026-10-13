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

        
        