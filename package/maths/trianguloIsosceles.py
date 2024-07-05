from package.maths.trianguloEquilatero import TrianguloEquilatero
from math import sqrt

class TrianguloIsosceles(TrianguloEquilatero):

    def __init__(self, x, y, lado, lado2):
        super().__init__(x, y, lado)
        self.lado2 = lado2

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