from package.maths.trianguloIsosceles import TrianguloIsosceles
from math import sqrt

class TrianguloEscaleno(TrianguloIsosceles):

    def __init__(self, x, y, lado1, lado2, lado3):
        super().__init__(x, y, lado1, lado2)
        if lado3 != lado2 and lado3 != lado1 and lado3 < lado1 + lado2:
            self.lado3 = lado3
        else:
            self.lado3 = (lado1 * 2) - 2

    def perimetro(self):
        return self.lado3 + self.lado1 + self.lado2
    
    def area(self):
        semiPerimetro = self.perimetro() / 2
        return sqrt(semiPerimetro * (semiPerimetro - self.lado1) * (semiPerimetro - self.lado2) * (semiPerimetro - self.lado3))
    
    def model(self):
        print('Posição: ({};{})\nMódulo: {:.2f}\nPerimetro: {}\nÁrea: {:.2f}'.format(self.get_x(), self.get_y(), self.modulo(), self.perimetro(), self.area()))