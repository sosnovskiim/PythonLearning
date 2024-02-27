from math import sqrt

a, b = map(int, input().split())
for n in range(a, b + 1):
    for d in range(2, int(sqrt(n)) + 1):
        if n % d == 0:
            break
    else:
        print(n, end=' ')
