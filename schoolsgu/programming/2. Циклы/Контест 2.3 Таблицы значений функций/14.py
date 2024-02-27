from math import sqrt
from math import log
from math import e

a, b, h = map(float, input().split())
x = a
while b - x > 10 ** -6 or abs(x - b) < 10 ** -6:
    print(f'{x:.6f}', end='\t')
    t, p = 4 - 2 * x, x ** 2 - 2 * x + 1
    if t > 0 and abs(log(t, e)) >= 10 ** -6 and (p > 0 or abs(p) < 10 ** -6):
        print(f'{sqrt(p) / log(t, e):.6f}')
    else:
        print('undefined')
    x += h
