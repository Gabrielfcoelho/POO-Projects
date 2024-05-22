from package.maths.ponto import Ponto
from math import pi


class Circulo(Ponto):

    def __init__(self, x, y, raio):
        super().__init__(x, y)
        self.__raio = raio

    def set_raio(self, raio):
        if str(raio).isnumeric() and raio > 0:
            self.__raio = raio
        else:
            self.__raio = 1

    def get_raio(self):
        return self.__raio

    def diametro(self):
        return self.__raio * 2

    def perimetro(self):
        return 2 * pi * self.__raio

    def area(self):
        return pi * self.__raio ** 2

    def model(self):
        print('Posição: ({};{})\nMódulo: {:.2f} \nRaio: {}'.format(self.get_x(), self.get_y(), self.modulo(), self.get_raio()))
        print('Diametro: {}\nPerimetro: {:.2f}\nÁrea: {:.2f}'.format(self.diametro(), self.perimetro(), self.area()))