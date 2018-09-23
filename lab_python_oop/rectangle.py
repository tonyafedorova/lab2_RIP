from lab_python_oop import figure


class Rectangle(figure.Figure):

    def __init__(self, height, width, colour, name="Rectangle"):
        self.height = height
        self.width = width
        self.colour = colour
        self.name = name

    def area(self):
        return self.width * self.height

    def __repr__(self):
        print("Высота прямоугольника = {0}, ширина прямоугольника = {1}".format(self.height, self.width))
        print("Площадь прямоугольника = {0}, цвет прямоугольника = {1}\n".format(self.area(), self.colour))

    def gn(self):
        return self.name
