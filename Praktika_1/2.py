input_number = int(input())
print("вводимое число четное" if input_number % 2 == 0 else "вводимое число нечетное")
print(
    "вводимое число положительное"
    if input_number > 0
    else "вводимое число отрицательное"
)
if input_number in [i for i in range(10, 51)]:
    print("вводимое число принадлежит отрезку от 10 до 50")
else:
    print("вводимое число не принадлежит отрезку от 10 до 50")
