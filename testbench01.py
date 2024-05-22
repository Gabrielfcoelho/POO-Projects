from package.maths.ponto import Ponto


def workspace():
    meu_primeiro_obj = Ponto(1, 1)
    meu_primeiro_obj.model()
    meu_primeiro_obj.set_x(2)
    meu_primeiro_obj.set_y(2)
    meu_primeiro_obj.model()


if __name__ == "__main__":
    workspace()
