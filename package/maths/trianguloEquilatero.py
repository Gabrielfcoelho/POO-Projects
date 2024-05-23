from package.maths.ponto import Ponto
from math import sqrt

class TrianguloEquilatero(Ponto):

    def __init__(self, x, y, lado):
        super().__init__(x, y)
        self.lado1 = lado
        self.n = 3

    def set_lado(self, lado):
        if str(lado).isnumeric() and lado > 0:
            self.lado1 = lado
        else:
            self.lado1 = 1

    def get_lado(self):
        return self.lado1

    def altura(self):
        return self.lado1 * sqrt(3) / 2
    
    def perimetro(self):
        return 3 * self.lado1
    
    def area(self):
        return self.altura() * self.lado1 / 2
    
    def numDiagonal(self):
        return self.n * (self.n - 3) / 2
    
    def AngulosInternos(self):
        return (self.n - 2) * 180
    
    def model(self):
        super().model()
        print('Altura: {:.2f}\nPerimetro: {}\nÁrea: {:.2f}'.format(self.altura(), self.perimetro(), self.area()))