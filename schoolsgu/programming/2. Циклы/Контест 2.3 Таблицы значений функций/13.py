from math import sqrt
from math import log
from math import e

a, b, h = map(float, input().split())
x = a
while b - x > 10 ** -6 or abs(x - b) < 10 ** -6:
    print(f'{x:.6f}', end='\t')
    t = 5 * x + 1
    if (t > 0 or abs(t) < 10 ** -6) and abs(sqrt(t)) >= 10 ** -6 and x - 2 > 0:
        print(f'{log(x - 2, e) / sqrt(t):.6f}')
    else:
        print('undefined')
    x += h
