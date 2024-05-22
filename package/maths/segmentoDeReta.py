from package.maths.ponto import Ponto

class Reta(Ponto):

    def __init__(self, x, y):
        super().__init__(x, y)

    def interpolar(self, x):
        y = self.x * x + self.y
        return y

    def model(self):
        super().model()