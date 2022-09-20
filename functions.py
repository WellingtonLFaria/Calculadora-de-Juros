class Juros_Simples():
    def __init__(self, capital = float, taxaj_porcentagem = int, tempo = int):
        self.J = float
        self.c = capital
        self.i = taxaj_porcentagem
        self.t = tempo
    

    def calcular(self):
        self.J = self.c * (self.i/100) * self.t
        return self.J


class Juros_Compostos():
    def __init__(self, capital = float, taxaj_porcentagem = int, tempo = int):
        self.J = float
        self.c = capital
        self.i = taxaj_porcentagem
        self.t = tempo
    

    def calcular(self):
        self.M = self.c*((1+(self.i/100))**self.t)
        self.J = self.M - self.c
        return self.J, self.M