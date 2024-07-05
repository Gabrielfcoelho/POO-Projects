from math import sqrt

class Ponto:

    def __init__(self, x = 0, y = 0):
            self.x = x
            self.y = y

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
        print('Posição : ({};{}) \nMódulo : {:.2f}'.format(self.x, self.y, self.modulo()))

    