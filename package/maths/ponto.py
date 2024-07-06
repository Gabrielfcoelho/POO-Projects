from math import sqrt

class Ponto:

    def __init__(self, x = 0, y = 0):
            self.x = x
            self.y = y

    def __str__(self):
        return f'Ponto({self.x};{self.y})'
    
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, x):
        if str(x).isnumeric() and x >= 0:
            self._x = x
        else:
            self._x = 0

    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, y):
        if str(y).isnumeric() and y >= 0:
            self._y = y
        else:
            self._y = 0

    def modulo(self):
        return sqrt(self._x ** 2 + self._y ** 2)
    
    def model(self):
        print(self.__str__())
        print(f'Distância até a origem : {self.modulo():.2f} un')

    def isNumber(self, n):
        try:
            float(n)
        except ValueError:
            return False
        return True

    