from package.maths.poligono import Poligono

class Pentagono(Poligono):

    def __init__(self, x, y, lado):
        super().__init__(x, y, lado)
        self.numLado = 5

    def __str__(self):
        return f'Pentágono com lado = {self.lado} un'
    
    @property
    def numLado(self):
        return self.__numLado
    
    @numLado.setter
    def numLado(self, x):
        if x == 5:
            self.__numLado = x
        else:
            self.__numLado = 5
