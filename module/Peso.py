
class Peso:
    def __init__(self,altura):
        self.altura = altura

    def homem(self):
        return (72.7*self.altura)-58

    def mulher(self):
        return (62.1*self.altura)-44.7
