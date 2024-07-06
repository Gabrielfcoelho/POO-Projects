from package.maths.icosagono import Icosagono

def workspace():
    icosagono = Icosagono(3, 4, 10)
    icosagono.model()
    print(icosagono)

if __name__ == '__main__':
    workspace()