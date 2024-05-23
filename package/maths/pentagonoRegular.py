from package.maths.quadrado import Quadrado
from math import tan, radians

class Pentagono(Quadrado):

    def __init__(self, x, y, lado):
        super().__init__(x, y, lado)
        self.n += 1

    def perimetro(self):
        return (super().perimetro()) + self.lado1
    
    def numDiagonal(self):
        return self.n * (self.n - 3) / 2
    
    def AngulosInternos(self):
        return (self.n - 2) * 180 / self.n
    
    def apotema(self):
        return (self.lado1 / 2) / (tan(radians(36)))
    
    def area(self):
        return self.apotema() * self.perimetro() / 2
    
    def model(self):
        print('Perimetro: {}\nÁrea: {:.2f}\nNúmero de diagonais: {}\nMedida dos ângulos internos: {}'.format(self.perimetro(), self.area(), self.numDiagonal(), self.AngulosInternos()))
