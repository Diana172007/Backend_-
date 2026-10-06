input_str = input().lower()
count = {}
for i in input_str:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
count_reverse = []
for i in count:
    count_reverse.append((count[i], i))
count_reverse.sort()
count_reverse.reverse()
print(count_reverse[:3])
