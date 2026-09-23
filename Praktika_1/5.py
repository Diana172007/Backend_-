N = int(input())
array = [i for i in range(2, N + 1)]
copy1, copy2 = array, array
for i in copy1:
    for x in copy2:
        if i != x and x % i == 0:
            array.remove(x)
print(array)
