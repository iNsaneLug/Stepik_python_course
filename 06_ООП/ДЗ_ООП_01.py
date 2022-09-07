# Создать класс Name, который принимает имя и фамилию в качестве аргументов при конструировании.
#
# Класс должен поддерживать атрибуты:
#
# first_name, возвращающий имя
#
# last_name, возвращающий фамилию
#
# full_name, возвращающий имя и фамилию
#
# initials, возвращающий инициалы
#
# Класс должен приводить переданные имя и фамилию в форму при которой имя и фамилия начинаются с заглавной буквы,
# а все остальные буквы в нижнем регистре (поскольку вызывающий код может передавать такие строки как "JOHN", 'jOHN',
# 'sMiTh' и т.д.)
#
# Примеры вызовов:
#
# a1 = Name('john', 'SMITH')
# a1.first_name ➞ 'John'
# a1.last_name ➞ 'Smith'
# a1.full_name ➞ 'John Smith'
# a1.initials ➞ 'J.S'


class Name:
    def __init__(self, first_name, last_name):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.full_name = first_name.title() + ' ' + last_name.title()
        self.initials = first_name.title()[0] + '.' + last_name.title()[0]
