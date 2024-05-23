from package.maths.quadrado import Quadrado

def workspace():
    meu_quinto_obj = Quadrado(2, 2, 20)
    meu_quinto_obj.model()
    print(meu_quinto_obj.n)

if __name__ == "__main__":
    workspace()