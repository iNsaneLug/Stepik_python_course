# Напишите функцию any_duplicates, которая принимает двумерный массив размера 3х3 (9 элементов).
# Двумерный массив заполнен числами от 1 до 9.
#
# Функция должна вернуть False, если в массиве все числа от 1 до 9
# встречаются ровно один раз. В противном случае True.
#
# Примеры вызовов.
#
# any_duplicates([[1, 3, 2], [9, 7, 8], [4, 5, 6]]) ➞ False
# any_duplicates([[8, 9, 2], [5, 6, 1], [3, 7, 4]]) ➞ False
# any_duplicates([[1, 1, 3], [6, 5, 4], [8, 7, 9]]) ➞ True # 1 дублируется
# any_duplicates([[1, 2, 3], [3, 4, 5], [9, 8, 7]]) ➞ True # 3 дублируется
#
# Sample Input:
#
# 1 3 2,9 7 8,4 5 6
# Sample Output:
#
# False


def any_duplicates(sud):
    lst = [i for x in sud for i in x]
    return sorted(lst) != [1, 2, 3, 4, 5, 6, 7, 8, 9]


if __name__ == '__main__':
    input_str = [1, 3, 2], [9, 7, 8], [4, 5, 6]
    sq = [[int(x[0]), int(x[1]), int(x[2])] for x in input_str]
    result = any_duplicates(sq)
    print(result)
