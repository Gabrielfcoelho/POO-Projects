from package.maths.poligono import Poligono

class Pentagono(Poligono):

    def __init__(self, x, y, lado):
        super().__init__(x, y, lado)
        self.numLado = 5

    @property
    def numLado(self):
        return self._numLado
    
    @numLado.setter
    def numLado(self, x):
        if x == 5:
            self._numLado = x
        else:
            self._numLado = 5

    def model(self):
        print('Perimetro: {}\nÁrea: {:.2f}\nNúmero de diagonais: {}\nMedida dos ângulos internos: {}'.format(self.perimetro(), self.area(), self.numDiagonal(), self.AngulosInternos()))
