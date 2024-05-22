from package.maths.circulo import Circulo


def workspace():
    meu_segundo_obj = Circulo(2, 2, 5)
    meu_segundo_obj.model()
    meu_segundo_obj.set_x(4)
    meu_segundo_obj.set_y(4)
    meu_segundo_obj.set_raio(10)
    meu_segundo_obj.model()


if __name__ == "__main__":
    workspace()
