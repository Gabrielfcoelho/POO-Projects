from package.maths.triangulo import Triangulo


def workspace():
    meu_quarto_obj = Triangulo(2, 3, 5)
    print(meu_quarto_obj.altura())
    print(meu_quarto_obj.perimetro())
    print(meu_quarto_obj.area())

if __name__ == '__main__':
    workspace()