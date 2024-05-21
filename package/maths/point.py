class Point:

    def __init__(self, x, y):
        if x.isnumeric() and x >= 0:
            self.x= x
        else:
            self.x = 0
        if y.isnumeric() and y >= 0:
            self.y = y
        else:
            self.y = 0

    def set_x(self, x):
        if x.isnumeric() and x >= 0:
            self.x= x
        else:
            self.x = 0

    def set_y(self, y):
        if y.isnumeric() and y >= 0:
            self.y = y
        else:
            self.y = 0

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def model(self):
        print('Posição : ({};{})'.format(self.x, self.y))

