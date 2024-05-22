from package.maths.trianguloEquilatero import TrianguloEquilatero
from package.maths.ponto import Ponto
from math import sqrt

class Quadrado(TrianguloEquilatero):

    def __init__(self, x, y, lado):
        super().__init__(x, y, lado)

    def perimetro(self):
        return self.lado1 * 4
    
    def area(self):
        return self.lado1 ** 2
    
    def diagonal(self):
        return self.lado1 * sqrt(2)

    def model(self):
        Ponto.model(self)
        print('Perimetro: {}\nÁrea: {}\nDiagonal: {:.2f}'.format(self.perimetro(), self.area(), self.diagonal()))