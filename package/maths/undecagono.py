from package.maths.poligono import Poligono

class Undecagono(Poligono):

    def __init__(self, x, y, lado):
        super().__init__(x, y, lado)
        self.numLado = 11

    def __str__(self):
        return f'Undecágono com lado = {self.lado} un'
    
    @property
    def numLado(self):
        return self.__numLado
    
    @numLado.setter
    def numLado(self, x):
        if x == 11:
            self.__numLado = x
        else:
            self.__numLado = 11