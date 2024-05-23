from package.maths.pentagonoRegular import Pentagono

def workspace():
    meu_obj = Pentagono(2, 2, 20)
    meu_obj.model()
    print(meu_obj.n)

if __name__ == '__main__':
    workspace()