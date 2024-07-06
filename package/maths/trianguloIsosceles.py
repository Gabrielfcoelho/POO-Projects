from package.maths.ponto import Ponto
from math import sqrt

class TrianguloIsosceles(Ponto):

    def __init__(self, x, y, lado, lado2):
        self.ponto = Ponto(x, y)
        self.lado = lado
        self.lado2 = lado2

    @property
    def lado(self):
        return self._lado

    @lado.setter
    def lado(self, lado):
        if str(lado).isnumeric() and lado > 0:
            self._lado = lado
        else:
            self._lado = 1

    @property
    def lado2(self):
        return self._lado2
    
    @lado2.setter
    def lado2(self, lado2):
        if lado2 < (self.lado * 2) and lado2 != self.lado:
            self._lado2 = lado2
        else:
            self._lado2 = (self.lado * 2) - 1

    def altura(self):
        return sqrt(self.lado ** 2 - (self.lado2 / 2) ** 2)
    
    def perimetro(self):
        return self.lado * 2 + self.lado2
    
    def area(self):
        return self.lado2 * self.altura() / 2
    
    def model(self):
        super().model()

    def __str__(self):
        return super().__str__()