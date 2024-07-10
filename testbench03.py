from package.maths.circulo import Circulo


def workspace():
    circulo = Circulo(2, 2, 5)
    circulo.model()
    circulo.x = -1
    circulo.y = -1
    circulo.raio = -5
    circulo.model()


if __name__ == "__main__":
    workspace()
