# Написать функцию is_full_house, которая принимает список карт (руку, 5 карт иначе говоря) и определяет наличие
# комбинации Full House на руке. Возвращает True, если определён Full House, в противном случае - False.
#
# Full House это когда из пяти карт 2 одного достоинства и 3 одного достоинства (но отличающегося от пары).
#
# A - туз, J - валет, Q - дама, K - король, 2-10.
#
# Примеры Full House: (A, A, Q, Q, Q), (10, 10, 10, J, J)
#
# Примеры вызовов и возвратов:
#
# is_full_house(["A", "A", "A", "K", "K"]) ➞ True
# is_full_house(["3", "J", "J", "3", "3"]) ➞ True
# is_full_house(["10", "J", "10", "10", "10"]) ➞ False
# is_full_house(["7", "J", "3", "4", "2"]) ➞ False
#
# Sample Input:
#
# A A A K K
# Sample Output:
#
# True

def is_full_house(hand):
    return all([hand.count(i) >= 2 for i in hand])


lst = ["A", "A", "A", "K", "K"]
print(is_full_house(lst))

