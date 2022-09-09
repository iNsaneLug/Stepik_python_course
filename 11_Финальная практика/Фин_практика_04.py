# Написать функцию check_sequence, принимающую список целых чисел и возвращающую 1 если последовательность строго
# возрастающая, -1 если строго убывающая, 0 если ни то, ни другое.
#
# Примеры вызовов и возвратов:
#
# check_sequence([1, 2, 3]) ➞ 1
# check_sequence([3, 2, 1]) ➞ -1
# check_sequence([1, 2, 1]) ➞ 0
# check_sequence([1, 1, 2]) ➞ 0 # потому что 1 по индексу 1 не больше 1 по индексу 0
#
# Примечание: входящие списки содержат минимум 2 числа.
#
# Sample Input:
#
# 1 2 3
# Sample Output:
#
# 1


def check_sequence(lst):
    if sorted(set(lst)) == lst:
        return 1
    elif sorted(set(lst), reverse=True) == lst:
        return -1
    return 0


input_str = [1, 2, 3]
lst = [int(x) for x in input_str]

print(check_sequence(lst))
