def to_roman(s):
    """
    Переводит из арабских чисел в римские
    Args:
        s list[str]:  массив чисел хаписанных в римской форме
    Returns:
        list[int]: Функция возвращает массив арабсикх чисел
        
    """ ""
    result = []
    for n in s:
        thousands = ["", "M", "MM", "MMM"]
        hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        result.append(
            thousands[n // 1000]
            + hundreds[(n % 1000) // 100]
            + tens[(n % 100) // 10]
            + ones[n % 10]
        )
    return result


def end_roman(s):
    """
    Переводит из римских цифр в арабские
    Args:
    s list[str]:  массив чисел хаписанных в римской форме
    Returns:
    list[int]: Функция возвращает массив арабсикх чисел

    """
    result = []
    for i in s:
        j = 0
        k = 0
        while j != len(i):
            if j + 1 != len(i) and (
                (i[j] == "I" and i[j + 1] in "VX")
                or (i[j] == "X" and i[j + 1] in "LC")
                or (i[j] == "C" and i[j + 1] in "DM")
            ):
                if i[j] == "I":
                    k -= 1
                if i[j] == "X":
                    k -= 10
                if i[j] == "C":
                    k -= 100
            else:
                if i[j] == "M":
                    k += 1000
                if i[j] == "D":
                    k += 500
                if i[j] == "C":
                    k += 100
                if i[j] == "L":
                    k += 50
                if i[j] == "X":
                    k += 10
                if i[j] == "V":
                    k += 5
                if i[j] == "I":
                    k += 1
            j += 1
        result.append(k)
    return result


roman_tests = ["IV", "IX", "XLII", "XCIX", "MMXXIII"]
print(end_roman(roman_tests))

k = [1345, 50, 678, 123]
roman_tests = ["IV", "IX", "XLII", "XCIX", "MMXXIII"]
print(to_roman(k))
print(end_roman(roman_tests))
