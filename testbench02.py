from package.maths.reta import Reta


def workspace():
    meu_primeiro_obj = Reta(2, 2)
    meu_primeiro_obj.model()
    print('interpolar(5) = {}'.format(meu_primeiro_obj.interpolar(5)))
    meu_primeiro_obj.set_x(4)
    meu_primeiro_obj.set_y(4)
    meu_primeiro_obj.model()
    print('interpolar(5) = {}'.format(meu_primeiro_obj.interpolar(5)))


if __name__ == "__main__":
    workspace()
