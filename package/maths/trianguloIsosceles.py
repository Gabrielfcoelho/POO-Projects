from package.maths.retangulo import Retangulo
from math import sqrt

class trianguloIsosceles(Retangulo):

    def __init__(self, x, y, lado, ladoMenor):
        super().__init__(x, y, lado, ladoMenor)

    def altura(self):
        return sqrt(self.lado1 ** 2 - (self.lado2 / 2) ** 2)
    
    def perimetro(self):
        return self.lado1 * 2 + self.lado2
    
    def area(self):
        return self.lado2 * self.altura() / 2
    
    def model(self):
        return super().model()