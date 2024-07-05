from package.maths.trianguloEquilatero import TrianguloEquilatero
from package.maths.ponto import Ponto


def workspace():
    meu_quarto_obj = TrianguloEquilatero(3, 4, 5)
    meu_quarto_obj.model()
    print(meu_quarto_obj.apotema())
    

if __name__ == '__main__':
    workspace()