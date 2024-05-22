from package.maths.trianguloEquilatero import TrianguloEquilatero
from package.maths.quadrado import Quadrado
from math import sqrt


class Retangulo(TrianguloEquilatero):

    def __init__(self, x, y, lado1, lado2):
        super().__init__(x, y, lado1)
        if lado2 != lado1:
            self.lado2 = lado2
        else:
            self.lado2 = lado1 + 1

    def set_lado2(self, lado2):
        if str(lado2).isnumeric() and lado2 > 0:
            self.lado2 = lado2
        else:
            self.lado2 = 1
    
    def get_lado2(self):
        return self.lado2
    
    def perimetro(self):
        return 2 * self.lado1 + 2 * self.lado2
    
    def area(self):
        return self.lado1 * self.lado2
    
    def diagonal(self):
        return sqrt(self.lado1 ** 2 + self.lado2 ** 2)
    
    def model(self):
        Quadrado.model(self)