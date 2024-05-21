from package.maths.triangulo import Triangulo

class Square(Triangulo):

    def __init__(self, x, y, lado):
        super().__init__(x, y, lado)

    def perimetro(self):
        return self.lado * 4
    
    def area(self):
        return self.lado ** 2
    
    def diagonal(self):
        return self.lado * (2 ** (1/2))

    def model(self):
        return super().model()