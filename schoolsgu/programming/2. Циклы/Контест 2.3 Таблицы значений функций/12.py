from math import log
from math import e

a, b, h = map(float, input().split())
x = a
while b - x > 10 ** -6 or abs(x - b) < 10 ** -6:
    print(f'{x:.6f}', end='\t')
    if x ** 4 - 1 > 0 and 1 + x > 0:
        print(f'{log(x ** 4 - 1, e) * log(1 + x, e):.6f}')
    else:
        print('undefined')
    x += h
