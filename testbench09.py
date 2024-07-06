from package.maths.pentagono import Pentagono

def workspace():
    pentagono = Pentagono(2, 2, 20)
    pentagono.model()
    print(pentagono)

if __name__ == '__main__':
    workspace()