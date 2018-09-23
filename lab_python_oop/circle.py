from lab_python_oop import figure
import math


class Circle(figure.Figure):
    def __init__(self, radius, col, name="Circle"):
        self.colour = col
        self.radius = radius
        self.name = name

    def area(self):
        return math.pi * self.radius * self.radius

    def __repr__(self):
        print("Сторона круга = {0}, площадь круга = {1}, цвет круга = {2}\n".format(self.radius, self.area(), self.colour))

    def gn(self):
        return self.name
