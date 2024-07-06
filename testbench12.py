from package.maths.octogono import Octogono

def workspace():
    octogono = Octogono(3, 4, 10)
    octogono.model()
    print(octogono)

if __name__ == '__main__':
    workspace()