from math import sqrt
from math import log
from math import e

a, b, h = map(float, input().split())
x = a
while b - x > 10 ** -6 or abs(x - b) < 10 ** -6:
    print(f'{x:.6f}', end='\t')
    t = 2 * x ** 5 - 1
    if abs(3 * x) >= 10 ** -6 and (t > 0 or abs(t) < 10 ** -6):
        print(f'{log(abs(3 * x), e) * sqrt(t):.6f}')
    else:
        print('undefined')
    x += h
