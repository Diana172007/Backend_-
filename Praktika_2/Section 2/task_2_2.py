"""Печатает, вошёл ли Стас в тройку лидеров."""


def check_winners(scores, student_score):
    """
    Печатает, вошёл ли Стас в тройку лидеров.
     Args:
        scores (list[int]): Список баллов всех участников олимпиады.
            Баллы могут повторяться.
        student_score (int): Количество баллов, которое набрал Стас.

    Returns:
        None: Функция ничего не возвращает, только печатает результат.
    """
    sorted_scores = sorted(scores)[::-1]
    result = []

    for i in sorted_scores:
        if i not in result and len(result) != 3:
            result.append(i)

    if student_score in result:
        print("Вы в тройке победителей!")
    else:
        print("Вы не попали в тройку победителей.")


# Проверка
check_winners([3, 5, 8, 1, 35, 6, 3, 8], 5)
