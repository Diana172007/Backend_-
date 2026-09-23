N = int(input())
length = 1
start = 1
count = 9
while N > length * count:
    N -= length * count
    length += 1
    start *= 10
    count *= 10
number = start + (N - 1) // length
index = (N - 1) % length
print(str(number)[index])
