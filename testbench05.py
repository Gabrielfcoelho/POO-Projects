from package.maths.quadrado import Quadrado

def workspace():
    meu_quinto_obj = Quadrado(3, 4, 20)
    meu_quinto_obj.model()
    print(meu_quinto_obj.apotema())

if __name__ == "__main__":
    workspace()