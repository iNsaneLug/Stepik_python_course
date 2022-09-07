# Создайте класс Pizza, который принимает список ингредиентов.
#
# Класс поддерживает:
#
# - атрибут order_number, который возвращает текущий номер заказа
# (подсказка: используйте статический атрибут в качестве сквозного счётчика)
#
# - атрибут ingredients, который возвращает список, принятый в конструкторе
#
# - функции (garden_feast, hawaiian, meat_festival) создания видов пицц,
# ингредиенты которых заранее известны (см. таблицу)
#
# Name              Ingredients
#
# hawaiian        - ham, pineapple
# meat_festival   - beef, meatball, bacon
# garden_feast    - spinach, olives, mushroom
#
# Примеры вызовов:
#
# p1 = Pizza(['bacon', 'parmesan', 'ham'])   # order 1
# p2 = Pizza.garden_feast()                  # order 2
# p1.ingredients ➞ ['bacon', 'parmesan', 'ham']
# p2.ingredients ➞ ['spinach', 'olives', 'mushroom']
# p1.order_number ➞ 1
# p2.order_number ➞ 2


class Pizza:
    order = 0
    ingredients = []

    def __init__(self, ingredients=None):
        if ingredients:
            self.ingredients = ingredients
        else:
            print("")

    @classmethod
    def hawaiian(cls):
        cls.hawaiian = ['ham', 'pineapple']
        cls.ingredients = cls.hawaiian

    @classmethod
    def meat_festival(cls):
        cls.meat_festival = ['beef', 'meatball', 'bacon']
        cls.ingredients = cls.meat_festival

    @classmethod
    def garden_feast(cls):
        cls.garden_feast = ['spinach', 'olives', 'mushroom']
        cls.ingredients = cls.garden_feast

    @classmethod
    def order_number(cls):
        cls.order += 1
        return print(cls.order)
