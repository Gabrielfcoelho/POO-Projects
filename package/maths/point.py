class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_x(self, x):
        if str(x).isnumeric() and x >= 0:
            self.x= x
        else:
            self.x = 0

    def set_y(self, y):
        if str(y).isnumeric() and y >= 0:
            self.y = y
        else:
            self.y = 0

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def model(self):
        print('Posição : ({};{})'.format(self.x, self.y))

