from lab_python_oop import rectangle


class Square(rectangle.Rectangle):
    def __init__(self, width, col, name="Square"):
        self.width = width
        self.colour = col
        self.name = name

    def area(self):
        return self.width * self.width

    def __repr__(self):
        print("Сторона квадрата = {0}, площадь квадрата = {1}, цвет квадрата = {2}\n".format(self.width, self.area(), self.colour))

    def gn(self):
        return self.name
