from package.maths.retangulo import Retangulo
from math import sqrt

class TrianguloEscaleno(Retangulo):

    def __init__(self, x, y, ladoMaior, lado, ladoMenor):
        super().__init__(x, y, lado, ladoMenor)
        self.ladoMaior = ladoMaior

    def perimetro(self):
        return self.ladoMaior + self.lado1 + self.lado2
    
    def area(self):
        semiPerimetro = self.perimetro() / 2
        return sqrt(semiPerimetro * (semiPerimetro - self.lado1) * (semiPerimetro - self.ladoMaior) * (semiPerimetro - self.lado2))
    
    def model(self):
        return super().model()