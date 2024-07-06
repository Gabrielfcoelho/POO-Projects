from package.maths.undecagono import Undecagono

def workspace():
    undecagono = Undecagono(3, 4, 10)
    undecagono.model()
    print(undecagono)

if __name__ == '__main__':
    workspace()