from math import sqrt

a, b, h = map(float, input().split())
x = a
while b - x > 10 ** -6 or abs(x - b) < 10 ** -6:
    print(f'{x:.6f}', end='\t')
    t, p = x ** 3 - 1, x ** 2 - 1
    if (t > 0 or abs(t) < 10 ** -6) and (p > 0 or abs(p) < 10 ** -6) and abs(sqrt(p)) >= 10 ** -6:
        print(f'{sqrt(t) / sqrt(p):.6f}')
    else:
        print('undefined')
    x += h
