from package.maths.ponto import Ponto


def workspace():
    ponto = Ponto(-1, -1)
    ponto.model()
    ponto.x = 2
    ponto.y = 2
    ponto.model()



if __name__ == "__main__":
    workspace()
