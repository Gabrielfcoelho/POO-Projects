from package.maths.straightLine import straightLine


def workspace():
    meu_primeiro_obj = straightLine(2, 4)
    meu_primeiro_obj.model()
    print('interpolar(5) = {}'.format(meu_primeiro_obj.interpolar(5)))


if __name__ == "__main__":
    workspace()