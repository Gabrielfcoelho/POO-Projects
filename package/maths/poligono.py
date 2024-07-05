from package.maths.ponto import Ponto
from math import tan, radians

class Poligono:

    def __init__(self, x, y, lado):
        self.ponto = Ponto(x, y) 
        self.lado = lado

    @property
    def numLado(self):
        return self._numLado
    
    @numLado.setter
    def numLado(self, x):
        if x >= 3:
            self._numLado = x
        else:
            self._numLado = 3
    
    @property
    def lado(self):
        return self._lado
    
    @lado.setter
    def lado(self, lado):
        if str(lado).isnumeric() and lado > 0:
            self._lado = lado
        else:
            self._lado = 1

    def perimetro(self):
        return self.numLado * self.lado

    def area(self):
       return self.apotema() * self.perimetro() / 2

    def numDiagonal(self):
        return self.numLado * (self.n - 3) / 2
    
    def anguloInterno(self):
        return (self.numLado - 2) * 180

    def apotema(self):
        return (self.lado / 2) / (tan(radians(360 / (self.numLado * 2))))

    def model(self):
        pass

    def __str__(self):
        pass