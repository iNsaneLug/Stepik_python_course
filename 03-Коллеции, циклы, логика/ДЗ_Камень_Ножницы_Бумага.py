# Написать игру в "камень-ножницы-бумага" против компьютера.
#
# Запустить игру в бесконечном цикле. Запросить ввод от пользователя (R - камень, S - ножницы, P - бумага).
# Сгенерировать случайный выбор компьютера. Вывести выбор компьютера. Определить победителя, выведя соответствующую информацию.
# Спросить пользователя - хочет ли он повторить игру. Если хочет - повторить, не хочет - выйти из цикла.


import random

while True:
    user_action = input("Сделайте выбор — камень К, ножницы Н или бумага Б: ")
    possible_actions = ["К", "Н", "Б"]
    computer_action = random.choice(possible_actions)
    print(f"\nВы выбрали {user_action}, компьютер выбрал {computer_action}.\n")
    if user_action == computer_action:
        print(f"Оба пользователя выбрали {user_action}. Ничья!!")
    elif user_action == "К":
        if computer_action == "Н":
            print("Камень бьет ножницы! Вы победили!")
        else:
            print("Бумага оборачивает камень! Вы проиграли.")
    elif user_action == "Б":
        if computer_action == "К":
            print("Бумага оборачивает камень! Вы победили!")
        else:
            print("Ножницы режут бумагу! Вы проиграли.")
    elif user_action == "S":
        if computer_action == "Б":
            print("Ножницы режут бумагу! Вы победили!")
        else:
            print("Камень бьет ножницы! Вы проиграли.")
    play_again = ""
    play_again = input("Сыграем еще? (д/н): ")
    if play_again.lower() != "д":
        break
