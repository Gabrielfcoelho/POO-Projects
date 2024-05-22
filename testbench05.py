from package.maths.retangulo import Retangulo

def workspace():
    meu_quinto_obj = Retangulo(2, 2, 20, 10)
    print(meu_quinto_obj.perimetro())
    print(meu_quinto_obj.area())

if __name__ == "__main__":
    workspace()