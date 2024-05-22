from package.maths.trianguloEscaleno import TrianguloEscaleno

def workspace():
    meu_setimo_obj = TrianguloEscaleno(2, 2, 5, 4, 3)
    print(meu_setimo_obj.perimetro())
    print(meu_setimo_obj.area())

if __name__ == "__main__":
    workspace()