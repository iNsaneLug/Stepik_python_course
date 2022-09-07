# Создать класс Employee, который принимает имя, фамилию и зарплату в качестве аргументов при конструировании.
#
# Класс должен поддерживать:
#
# - атрибут first_name, возвращающий имя
# - атрибут last_name, возвращающий фамилию
# - атрибут salary, возвращающий зарплату
#
# функцию from_string, которая принимает имя, фамилию и зарплату
# в формате 'first_name-last_name-salary', парсит строку и возвращает экземпляр Employee
#
# Примеры:
#
# emp1 = Employee('Mary', 'Sue', 60000)
# emp2 = Employee.from_string('John-Smith-55000')
#
# emp1.first_name ➞ 'Mary'
# emp1.salary ➞ 60000
# emp2.first_name ➞ 'John'
# emp2.salary ➞ 55000


class Employee:

    def __init__(self, f_name, l_name, salar):
        self.f_name = f_name
        self.l_name = l_name
        self.salar = salar

    @classmethod
    def from_string(cls, emp_str):
        f_name, l_name, salar = emp_str.split('-')
        return cls(f_name, l_name, salar)

    def first_name(self):
        return print(self.f_name)

    def last_name(self):
        return print(self.l_name)

    def salary(self):
        return print(self.salar)