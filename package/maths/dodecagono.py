from package.maths.poligono import Poligono

class Dodecagono(Poligono):

    def __init__(self, x, y, lado):
        super().__init__(x, y, lado)
        self.numLado = 12

    def __str__(self):
        return f'Dodecágono com lado = {self.lado} un'
    
    @property
    def numLado(self):
        return self.__numLado
    
    @numLado.setter
    def numLado(self, x):
        if x == 12:
            self.__numLado = x
        else:
            self.__numLado = 12