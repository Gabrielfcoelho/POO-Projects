from package.maths.eneagono import Eneagono 

def workspace():
    eneagono = Eneagono(3, 4, 10)
    eneagono.model()
    print(eneagono)

if __name__ == '__main__':
    workspace()