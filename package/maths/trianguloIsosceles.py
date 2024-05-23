from package.maths.trianguloEquilatero import TrianguloEquilatero
from math import sqrt

class TrianguloIsosceles(TrianguloEquilatero):

    def __init__(self, x, y, lado1, lado2):
        super().__init__(x, y, lado1)
        if lado2 < (lado1 * 2) and lado2 != lado1:
            self.lado2 = lado2
        else:
            self.lado2 = (lado1 * 2) - 1

    def altura(self):
        return sqrt(self.lado1 ** 2 - (self.lado2 / 2) ** 2)
    
    def perimetro(self):
        return self.lado1 * 2 + self.lado2
    
    def area(self):
        return self.lado2 * self.altura() / 2
    
    def model(self):
        super().model()