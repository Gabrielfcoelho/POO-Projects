from package.maths.point import Point
from math import pi


class Circle(Point):

    def __init__(self, x, y, raio):
        super().__init__(x, y)
        self.__raio = raio

    def set_raio(self, raio):
        if raio.isnumeric() and raio >= 1:
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
        print('Posição: ({};{}) \nRaio: {}'.format(self.x, self.y, self.__raio))