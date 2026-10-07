import random
position = [
    """
       -----
       |   |
           |
           |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|\\ |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|\\ | 
       |   |
      /    |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|\\ |
      / \\ |
           |
    =========""",
]

words = ["принцесса", "виселица", "алгоритм", "код", "магазин","курсы","интернет"]
max_mistakes = 6
secret = random.choice(words)
guessed = set()
mistakes = 0
"""
цикл игры: повторяется, пока не набрано максимальное количество ошибок (т.е 6 так как положение виселицы всего 6).
на каждой итерации: показываем виселицу и слово, проверяем победу,
спрашиваем букву, обновляем счётчики.
"""
while mistakes < max_mistakes:
    print(position[mistakes])
    view = ""
    for letter in secret:
        if letter in guessed:
            view += letter + " "
        else:
            view += "_ "
    print("слово:", view)
    print("ошибок:", mistakes, "из", max_mistakes)
    if "_" not in view:
        print(f"победа слово:{secret}")
        break
    print("буква: ")
    letter = input()
    guessed.add(letter)
    if letter in secret:
        print("такая буква есть")
    else:
        mistakes += 1
        print("такой буквы нет")
else:
    print(position[max_mistakes])
    print(f"вы проиграли, слово было {secret}")
