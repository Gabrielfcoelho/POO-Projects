from package.maths.triangulo import Triangulo


class Retangulo(Triangulo):

    def __init__(self, x, y, lado, ladoMenor):
        super().__init__(x, y, lado)
        self.ladoMenor = ladoMenor

    def set_ladoMenor(self, ladoMenor):
        if str(ladoMenor).isnumeric() and ladoMenor >= 0:
            self.ladoMenor = ladoMenor
        else:
            self.ladoMenor = 0
    
    def get_ladoMenor(self):
        return self.ladoMenor
    
    def perimetro(self):
        return 2 * self.lado + 2 * self.ladoMenor
    
    def area(self):
        return self.lado * self.ladoMenor
    
    def model(self):
        return super().model()