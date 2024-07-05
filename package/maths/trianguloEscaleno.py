from package.maths.trianguloIsosceles import TrianguloIsosceles
from math import sqrt

class TrianguloEscaleno(TrianguloIsosceles):

    def __init__(self, x, y, lado, lado2, lado3):
        super().__init__(x, y, lado, lado2)
        self.lado3 = lado3

    @property
    def lado3(self):
        return self._lado3
    
    @lado3.setter
    def lado3(self, lado3):
        if lado3 != self.lado2 and lado3 != self.lado and lado3 < self.lado + self.lado2:
            self._lado3 = lado3
        else:
            self._lado3 = (self.lado * 2) - 2

    def perimetro(self):
        return self.lado3 + self.lado + self.lado2
    
    def area(self):
        semiPerimetro = self.perimetro() / 2
        return sqrt(semiPerimetro * (semiPerimetro - self.lado) * (semiPerimetro - self.lado2) * (semiPerimetro - self.lado3))
    
    def model(self):
        print('Posição: ({};{})\nMódulo: {:.2f}\nPerimetro: {}\nÁrea: {:.2f}'.format(self.ponto.x, self.ponto.y, self.ponto.modulo(), self.perimetro(), self.area()))