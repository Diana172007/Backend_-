import random

alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
special = "!@#$%^&*()-_=+[]{};:,.<>?/|~"


def generate_password():
    """Генерирует пароль случайной длины из всех категорий символов.
    Args:
        в функцию ничего не передаеться
    Returns:
        str: функция возращает строку , являющаяся паролем
    """
    alphabet_new = alphabet + alphabet_upper + numbers + special
    length = random.randint(8, 1000)
    password = ""
    for _ in range(length):
        password += random.choice(alphabet_new)
    return password


print(generate_password())
