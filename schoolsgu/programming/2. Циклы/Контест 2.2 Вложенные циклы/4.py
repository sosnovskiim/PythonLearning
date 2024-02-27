from math import sqrt

n = int(input())
for i in range(100_000):
    a, b = n - i, n + i
    for d in range(2, int(sqrt(a)) + 1):
        if a % d == 0:
            break
    else:
        print(a)
        break
    for d in range(2, int(sqrt(b)) + 1):
        if b % d == 0:
            break
    else:
        print(b)
        break
