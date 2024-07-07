from package.maths.trianguloEquilatero import TrianguloEquilatero



def workspace():
    x = 'abobrinha'
    triangulo = TrianguloEquilatero(3, 4, x)
    triangulo.model()
    print(triangulo)
    if super(type, type(triangulo)) == Poligono:
            print('Sucesso!') 
    

if __name__ == '__main__':
    workspace()