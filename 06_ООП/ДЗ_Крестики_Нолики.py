# А вот и новое домашнее задание. Непростое. Но вполне реализуемое.
#
# Вы попробуете реализовать игру в крестики-нолики размером 3х3 - самые что ни наесть обыкновенные.
#
# Сделайте метод, который выводит на каждом ходу текущее положение с линейками,
# крестиками и ноликами (используйте буквы X и O в качестве крестиков и ноликов) -
# так игрокам будет удобнее ориентироваться. Подсказка: если надо вывести строку без
# перевода коретки на новую строку, используйте функцию print и передавайте параметр end=''.
#
# Также вам понадобится реализовать способ проверки наличия выигрышной комбинации. Подсказа: договоримся, что клетки
# поля будут пронумерованы от 0 до 8 и пользователи будут вводить индекс поля, чтобы поставить там крестик или нолик.
#
# Для упрощения - тот кто ходит первым - ставит крестик.


board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


def print_state(state):
    for i, c in enumerate(state):
        if (i + 1) % 3 == 0:
            print(f'{c}')
        else:
            print(f'{c}|', end='')


print_state(board)

winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]


def get_winner(state, combinations):
    for (x, y, z) in combinations:
        if state[x] == state[y] and state[y] == state[z] and (state[x] == 'X' or state[x] == 'O'):
            return state[x]
    return ''


def play_game(self):
    current_sign = 'X'
    while get_winner(self, winning_combinations) == '':
        index = int(input(f'Where you want to draw {current_sign}?'))
        self[index] = current_sign

        print_state(self)

        winner_sign = get_winner(self, winning_combinations)
        if winner_sign != '':
            print(f'We have a winner:{winner_sign}')

        current_sign = 'X' if current_sign == 'O' else 'O'


play_game(board)
