def solve(n):
    d = 1
    while n > 9 * 10 ** (d - 1) * d:
        n -= 9 * 10 ** (d - 1) * d
        d += 1
    first = 10 ** (d - 1)
    number = first + (n - 1) // d
    return str(number)[(n - 1) % d]


N = int(input())
print(solve(N))
