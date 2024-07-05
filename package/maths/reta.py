from package.maths.ponto import Ponto
from math import sqrt

class Reta:

    def __init__(self, x1, y1, x2, y2):
        self.ponto1 = Ponto(x1, y1)
        self.ponto2 = Ponto(x2, y2)

    def comprimento(self):
        return sqrt((self.ponto1.x - self.ponto2.x) ** 2 + (self.ponto1.y - self.ponto2.y) ** 2)
    
    def interpolar(self, x):
        y = self.x * x + self.y
        return y

    def model(self):
        super().model()