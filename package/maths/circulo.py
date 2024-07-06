from package.maths.ponto import Ponto
from math import pi


class Circulo(Ponto):

    def __init__(self, x, y, raio):
        super().__init__(x, y)
        self.raio = raio

    def __str__(self):
        return f'Círculo na posição ({self.x};{self.y}) e de raio {self.raio}'

    @property
    def raio(self):
        return self.__raio
    
    @raio.setter
    def raio(self, raio):
        if str(raio).isnumeric() and raio > 0:
            self.__raio = raio
        else:
            self.__raio = 1

    def diametro(self):
        return self.__raio * 2

    def perimetro(self):
        return 2 * pi * self.__raio

    def area(self):
        return pi * self.__raio ** 2

    def model(self):
        print(self.__str__())
        print(f'Diametro : {self.diametro()}')
        print(f'Perimetro : {self.perimetro():.2f}')
        print(f'Area : {self.area():.2f}')