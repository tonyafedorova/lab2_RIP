from lab_python_oop import rectangle
from lab_python_oop import square
from lab_python_oop import circle
from lab_python_oop import colour
import sys


def menu():
    print("Площадь чего вы хотите посчитать?")
    print("1)Прямоугольник")
    print("2)Квадрат")
    print("3)Круг")
    print("4)Выход")
    result = input()
    return result


work = True
# Обработка вводимых значений и вызов методов классов
while work:
    res = menu()
    if (res >= '1') and (res <= '4'):

        # Прямоугольник
        if res == '1':

            work1 = True
            while work1:
                print("Введите высоту:")
                try:
                    a = int(input())
                    work1 = False
                except (TypeError, ValueError):
                    print("Введите число!")

            work1 = True
            while work1:
                print("Введите ширину:")
                try:
                    b = int(input())
                    work1 = False
                except (TypeError, ValueError):
                    print("Введите число!")

            print("Введите цвет:")
            cool = colour.Colour()
            cool.v = input()
            rec = rectangle.Rectangle(a, b, cool.v)
            print(rec.gn())
            rec.__repr__()

        # Квадрат
        elif res == '2':
            work1 = True
            while work1:
                print("Введите сторону квадрата:")
                try:
                    a = int(input())
                    work1 = False
                except(TypeError, ValueError):
                    print("Введите число!")

            print("Введите цвет:")
            cool = colour.Colour
            cool.v = input()
            sq = square.Square(a, cool.v)
            print(sq.gn())
            sq.__repr__()

        # Круг
        elif res == '3':
            print("Введите радиус:")
            work1 = True
            while work1:
                try:
                    a = int(input())
                    work1 = False
                except(TypeError, ValueError):
                    print("Введите число!")

                print("Введите цвет:")
            cool = colour.Colour
            cool.v = input()
            cc = circle.Circle(a, cool.v)
            print(cc.gn())
            cc.__repr__()

        elif res == '4':
            work = False

    else:
        print("Вы ввели неверное значение!")
sys.exit()





