from package.maths.poligono import Poligono
from package.maths.circulo import Circulo
from math import sqrt

class Verificador:
    
    @classmethod
    def isCircunscrito(cls, poligono, circulo):
        if poligono.type() == Poligono and type(circulo) == Circulo:
            if poligono.apotema() == circulo.raio and poligono.ponto.x == circulo.x and poligono.ponto.y == circulo.y :
                return True
            else:
                return False
        else:
            raise TypeError('Classe dos argumentos inválida!')

    @classmethod
    def isInscrito(cls, circulo, poligono):
        if poligono.type() == Poligono and type(circulo) == Circulo:
            if sqrt(poligono.apotema() ** 2 + (poligono.lado / 2) ** 2) == circulo.raio and poligono.ponto.x == circulo.x and poligono.ponto.y == circulo.y :
                return True
            else:
                return False
        else:
            raise TypeError('Classe dos argumentos inválida!')
    