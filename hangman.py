import random

#  - - - - - - - - - СЮДА ПИШЕМ НОВЫЕ СЛОВА
WORDS = [
    "КОТ", "ПИТОН", "ПРОГРАММИРОВАНИЕ", "УНИВЕРСИТЕТ",
    "КОД", "АЛГОРИТМ", "ФУНКЦИЯ", "ИГРА", "КОМПЬЮТЕР"
]

#  - - - - - - - - - УВЕЛИЧИТЬ/УМЕНЬШИТЬ КОЛИЧЕСТВО ПОПЫТОК
MAX_ATTEMPTS = 6

#  - - - - - - - - - ВЫБОР СЛУЧАЙНОГО СЛОВА СО СПИСКА
def choose_word():
    return random.choice(WORDS)

#  - - - - - - - - - ПОКАЗ ТЕКУЩЕГО СОСТОЯНИЯ ИГРЫ
def display_state(secret_word, guessed_letters, attempts_left):
    display = []
    for letter in secret_word:
        if letter in guessed_letters:
            display.append(letter)
        else:
            display.append("_")
    print("\nСлово: ", " ".join(display))
    print("Оставшиеся попытки:", attempts_left)
    print("Использованные буквы:", " ".join(sorted(guessed_letters)) or "-")


def hangman_game():
    print("Добро пожаловать в игру 'Виселица'!")
    print("Я загадал слово. Попробуй отгадать его по буквам.\n")

    secret_word = choose_word()
    guessed_letters = set()
    attempts_left = MAX_ATTEMPTS

    unique_letters = set(secret_word)

    while attempts_left > 0:
        display_state(secret_word, guessed_letters, attempts_left)

        user_input = input("Введи одну букву (или 'quit' для выхода): ").strip().upper()

        if user_input.lower() == "quit":
            print("Игра завершена. Загаданное слово было:", secret_word)
            return

        if len(user_input) != 1 or not ("А" <= user_input <= "Я"):
            print("Некорректный ввод. Введи ОДНУ букву.")
            continue

        letter = user_input

        if letter in guessed_letters:
            print("Ты уже называл эту букву. Попробуй другую.")
            continue

        guessed_letters.add(letter)

        if letter in unique_letters:
            print("Есть такая буква!")
            if unique_letters.issubset(guessed_letters):
                display_state(secret_word, guessed_letters, attempts_left)
                print("\nПоздравляю! Ты отгадал слово:", secret_word)
                print("Победа!")
                return
        else:
            attempts_left -= 1
            print("Такой буквы нет. Ошибка.")

    print("\nПопытки закончились.")
    print("Ты проиграл. Загаданное слово было:", secret_word)


if __name__ == "__main__":
    hangman_game()
