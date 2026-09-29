N = int(input())
array = [i for i in range(2, N + 1)]
for i in array[:]:
    if i * i > N:
        break
    if i not in array:
        continue
    for x in array[:]:
        if x != i and x % i == 0:
            array.remove(x)

print(array)
