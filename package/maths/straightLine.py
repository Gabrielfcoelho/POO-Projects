from package.maths.point import Point

class straightLine(Point):
    def __init__(self, x, y):
        super().__init__(x, y)

    def interpolar(self, x):
        y = self.x * x + self.y
        return y

    def model(self):
        print('parâmetro: a = {} e b = {}'.format(self.x, self.y))