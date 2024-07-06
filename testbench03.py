from package.maths.circulo import Circulo


def workspace():
    circulo = Circulo(2, 2, 5)
    circulo.model()
    circulo.x = 4
    circulo.y = 4
    circulo.raio = 10
    circulo.model()
    print(circulo)


if __name__ == "__main__":
    workspace()
