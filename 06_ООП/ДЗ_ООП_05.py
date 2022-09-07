# 5. Окружность
# Создайте класс Circle который конструируется с передачей радиуса в качестве аргумента.
#
# Класс Circle должен предоставлять две функции:
#
# - get_area, которая возвращает площадь круга
# - get_perimeter, которая возвращает длину окружности
#
# # Примеры вызовов
#
# circle = Circle(10)
# area = circle.get_area() # возвращает 314.1592653589793
# perimeter = circle.get_perimeter() # возвращает 62.83184


import math


class circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


r = int(input("Введите радиус круга: "))

obj = circle(r)

print("Площадь круга:", round(obj.area(), 2))

print("Длина окружности:", round(obj.perimeter(), 2))
