# А теперь первое серьёзное домашнее задание. Вы попробуете разработать игру.
#
# Предлагаю древнюю китайскую игру в палочки.
#
# Играют два игрока.  Есть 10 палочек. Игроки по очереди берут от одной до трёх палочек.
# Играют до тех пор пока не закончатся палочки. Тот кто взял последним - тот проиграл.
#
# Реализуйте игру таким образом, чтобы могли играть два человека. Изначально есть 10 палочек. На каждом ходу выводите
# на консоль текущее количество оставшихся палочек и просите ввести количество палочек, которое хочет взять игрок (
# который делает ход). Не забывайте менять очерёдность игроков и сокращать кол-во палочек. В конце надо вывести кто
# победил - первый или второй игрок.
#
# Нюансы реализации могут отличаться. Кто-то может захотет запросить имена у игроков. Кто-то может захотеть
# реализовать не с 10-ю палочками, а с тем количеством, которое введёт пользователь (может он хочет играть с 20-ю
# палочками?).

def chinese_stick_game():
    sticks = int(input('Please input the amount of sticks to play with '))
    p1_name = input('Please player 1 tell me your name ')
    p2_name = input('Please player 2 tell me your name ')
    while sticks >= 1:
        p1_st_amount = int(input(p1_name + ' please choose a number between 1-3 '))
        sticks = sticks - p1_st_amount
        print(sticks, " stick(s) left...")
        if sticks <= 0:
            print(p1_name + ' you lost!')

        p2_st_amount = int(input(p2_name + ' please choose a number between 1-3 '))
        sticks = sticks - p2_st_amount
        print(sticks, " stick(s) left...")
        if sticks <= 0:
            print(p2_name + ' you lost!')


if __name__ == '__main__':
    chinese_stick_game()
