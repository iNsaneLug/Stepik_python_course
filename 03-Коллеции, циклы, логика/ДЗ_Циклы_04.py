# На вход подаются два списка. Например:
#
# first_list = [1, 2, 3, 4, 5]
# second_list = [11, 12, 13, 14, 15]
#
# Взять из первого списка все нечётные числа, из второго чётные и объединить их в новом списке.
#
# Примечание: можно сделать двумя циклами for, можно одним, можно с помощью list comprehensions.
#
# Sample Input:
#
# 2 3 4 5 6,10 11 12 13 14
# Sample Output:
#
# 3 5 10 12 14


a = [2, 3, 4, 5, 6]
b = [10, 11, 12, 13, 14]

listodds = [x for x in a if x % 2 != 0]
listevens = [x for x in b if x % 2 == 0]
joined_list = listodds + listevens

print(' '.join(map(str, joined_list)))
