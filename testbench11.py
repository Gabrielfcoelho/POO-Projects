from package.maths.heptagono import Heptagono

def workspace():
    heptagono = Heptagono(3, 4, 10)
    heptagono.model()
    print(heptagono)

if __name__ == '__main__':
    workspace()