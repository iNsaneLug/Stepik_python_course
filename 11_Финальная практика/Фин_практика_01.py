# . Напишите функцию count_vowels, которая принимает строку и возвращает количество гласных в ней.
#
# Примеры вызовов и возвратов:
#
# count_vowels('abcd') -> 1
# count_vowels('abcdef') -> 2
# count_vowels('bcd') -> 0
#
# Примечание: речь идёт только о латинском алфавите.
#
# Sample Input:
#
# abc
# Sample Output:
#
# 1


def count_vowels(str1):
    vowel = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for letter in str1:
        if letter in vowel:
            count += 1
    return print(count)


input_str = input(str())
count_vowels(input_str)
