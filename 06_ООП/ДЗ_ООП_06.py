# Создать класс Beverage, который при конструировании принимает список ингредиентов
#
# - поддерживает атрибут ingredients, возвращающий список ингредиентов, переданных при конструировании инстанции класса
#
# - поддерживает функцию get_cost, вычисляющую итоговую стоимость всех ингредиентов напитка
# (получается себестоимость напитка)
#
# - поддерживает функцию get_price, вычисляющую цену напитка посредством умножения себестоимости на 2.5
#
# - поддерживает функцию get_name, которая возвращает строку, перечисляющую ингредиенты, сортируя
# их в алфавитном порядке. Если ингредиентов больше одного, то в конце добавляет слово 'Fusion',
# иначе добавляет слово 'Smoothie'. Эта функция также должна заменять 'berries' на 'berry'.
#
# Ингредиенты и их себестоимость:
#
# Strawberries $1.50
# Banana $0.50
# Mango $2.50
# Blueberries $1.00
# Raspberries $1.00
# Apples $1.75
# Pineapple $3.50
#
#
# Примеры вызовов:
#
# s1 = Beverage(["Banana"])
# s1.ingredients ➞ ["Banana"]
# s1.get_cost() ➞ "$0.50"
# s1.get_price() ➞ "$1.25"
# s1.get_name() ➞ "Banana Smoothie"
#
# s2 = Beverage(["Raspberries", "Strawberries", "Blueberries"])
# s2.ingredients ➞ ["Raspberries", "Strawberries", "Blueberries"]
# s2.get_cost() ➞ "$3.50"
# s2.get_price() ➞ "$8.75"
# s2.get_name() ➞ "Blueberry Raspberry Strawberry Fusion"


prices = {"Strawberries": 1.50,
          "Banana": 0.50,
          "Mango": 2.50,
          "Blueberries": 1.00,
          "Raspberries": 1.00,
          "Apples": 1.75,
          "Pineapple": 3.50}


class Beverage:

    def __init__(self, ingredients):
        self.ingredients = ingredients
        self.cost = sum([prices[fruit] for fruit in self.ingredients])
        self.price = self.cost * 2.5

    def get_cost(self):
        return f'${self.cost:.2f}'

    def get_price(self):
        return f'${self.price:.2f}'

    def get_name(self):
        lst = sorted([i.replace('ies', 'y') for i in self.ingredients])
        return f'{" ".join(lst)} {"Fusion" if len(lst) > 1 else "Smoothie"}'
