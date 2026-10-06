RU = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
EN = "abcdefghijklmnopqrstuvwxyz"


def detect_language(text):
    ru = sum(1 for i in text if i in RU)
    en = sum(1 for i in text if i in EN)
    if ru > en:
        return RU
    return EN


def caesar(text, shift):
    alphabet = detect_language(text)
    result = ""
    for i in text:
        if i.lower() not in alphabet:
            result += i
            continue
        index = alphabet.index(i.lower())
        new_i = alphabet[(index + shift) % len(alphabet)]
        if i.isupper():
            result += new_i.upper()
        else:
            result += new_i
    return result
