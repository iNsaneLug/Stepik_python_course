# Два участника p1 и p2 участвуют в дуэли.
#
# Напишите функцию whos_first, которая принимает две строки и возвращает имя игрока, который выстрелил первым.
#
# Если игроки выстрелили одновременно, то вернуть строку "tie".
#
# Примеры вызовов и возвратов:
#
# whos_first(
#  "   Bang!        ",
#  "        Bang!   "
# ) ➞ "p1"
# # p1 стреляет быстрее p2
#
# whos_first(
#  "               Bang! ",
#  "             Bang!   "
# ) ➞ "p2"
# # p2 стреляет быстрее p1
#
# whos_first(
#  "     Bang!   ",
#  "     Bang!   "
# ) ➞ "tie"
# # ничья
#
# Примечание:
#
# передаваемые строки - могут быть различной длины! (то есть содержать различное количество пробелов).
#
# Sample Input:
#
#     Bang!    ,     Bang!
# Sample Output:
#
# p1


def whos_first(p1, p2):
    diff = p1.find('B') - p2.find('B')
    if diff < 0:
        return 'p1'
    elif diff > 0:
        return 'p2'
    else:
        return 'tie'


if __name__ == '__main__':
    p1 = '    Bang!    '
    p2 = '     Bang!   '
    result = whos_first(p1, p2)
    print(result)
