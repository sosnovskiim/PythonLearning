from math import sqrt

a, b, h = map(float, input().split())
x = a
while b - x > 10 ** -6 or abs(x - b) < 10 ** -6:
    print(f'{x:.6f}', end='\t')
    t = x ** 2 + 2 * x + 1
    if (t > 0 or abs(t) < 10 ** -6) and abs(sqrt(t)) >= 10 ** -6:
        print(f'{(3 * x + 4) / sqrt(t):.6f}')
    else:
        print('undefined')
    x += h
