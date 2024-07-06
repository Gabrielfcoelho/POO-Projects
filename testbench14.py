from package.maths.decagono import Decagono

def workspace():
    decagono = Decagono(3, 4, 10)
    decagono.model()
    print(decagono)

if __name__ == '__main__':
    workspace()