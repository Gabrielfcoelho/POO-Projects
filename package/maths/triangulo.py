from package.maths.point import Point

class Triangulo(Point):

    def __init__(self, x, y, lado):
        super().__init__(x, y)
        self.lado = lado

    def set_lado(self, lado):
        if str(lado).isnumeric() and lado >= 0:
            self.lado = lado
        else:
            self.lado = 0

    def get_lado(self):
        return self.lado

    def altura(self):
        return self.lado * (3**(1/2)) / 2
    
    def perimetro(self):
        return 3 * self.lado
    
    def area(self):
        return self.altura() * self.lado / 2
    
    def model(self):
        return super().model()