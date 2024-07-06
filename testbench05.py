from package.maths.quadrado import Quadrado

def workspace():
    quadrado = Quadrado(3, 4, 20)
    quadrado.model()
    print(quadrado.apotema())

if __name__ == "__main__":
    workspace()