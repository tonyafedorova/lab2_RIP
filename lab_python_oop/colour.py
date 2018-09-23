class Colour:
    def __init__(self):
        self.col = None

    def ge(self):
        return self.col

    def se(self, value):
        self.col = value

    def de(self):
        None

    v = property(ge, se, de, "Цвет")
