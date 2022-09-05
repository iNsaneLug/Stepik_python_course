# Построить цикл от 0 до введённого числа (включительно) и посчитать сумму всех чисел, делимых без остатка на 3 или 5. Вывести результат на консоль через print().
#
# Примечание: задача решается как прямым for, так и с помощью list comprehension (просуммировать числа списка можно, передав список в функцию sum(arg_list)).
#
# Sample Input:
#
# 10
# Sample Output:
#
# 33


number = int(input('Please select a number:'))
print(sum([number for number in range(number + 1) if number % 3 == 0 or number % 5 == 0]))
