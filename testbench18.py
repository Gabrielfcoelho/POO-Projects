from package.maths.quadrado import Quadrado
from package.maths.circulo import Circulo 
from math import sqrt
from package.maths.verificador import Verificador

def workspace():
    quadrado = Quadrado(10, 10, 4)
    circulo = Circulo(10, 10, 2)
    circulo2 = Circulo(10, 10, sqrt(8))


    print(Verificador.isCircunscrito(quadrado, circulo))
    print(Verificador.isInscrito(circulo2, quadrado))



if __name__ == '__main__':
    workspace()
