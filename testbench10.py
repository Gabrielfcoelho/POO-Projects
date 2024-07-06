from package.maths.hexagono import Hexagono

def workspace():
    hexagono = Hexagono(3, 4, 10)
    hexagono.model()
    print(hexagono)

if __name__ == '__main__':
    workspace()