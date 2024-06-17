from math import sqrt

class Ponto:

    def __init__(self, x = 0, y = 0):
            self.x = x
            self.y = y

    def set_x(self, x):
        if str(x).isnumeric() and x >= 0:
            self.x= x
        else:
            self.x = 0

    def set_y(self, y):
        if str(y).isnumeric() and y >= 0:
            self.y = y
        else:
            self.y = 0

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y
    
    def modulo(self):
        return sqrt(self.x ** 2 + self.y ** 2)
    
    def model(self):
        print('Posição : ({};{}) \nMódulo : {:.2f}'.format(self.get_x(), self.get_y(), self.modulo()))

