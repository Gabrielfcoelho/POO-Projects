from package.maths.reta import Reta


def workspace():
    reta = Reta(0, 0, 3, 4)
    print(reta)
    reta.model()


if __name__ == "__main__":
    workspace()
