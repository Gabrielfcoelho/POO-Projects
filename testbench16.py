from package.maths.dodecagono import Dodecagono

def workspace():
    dodecagono = Dodecagono(3, 4, 10)
    dodecagono.model()
    print(dodecagono)

if __name__ == '__main__':
    workspace()