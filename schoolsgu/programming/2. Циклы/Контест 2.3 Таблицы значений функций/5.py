from math import log
from math import e

a, b, h = map(float, input().split())
x = a
while b - x > 10 ** -6 or abs(x - b) < 10 ** -6:
    print(f'{x:.6f}', end='\t')
    t = x - 1
    if t > 0:
        print(f'{log(t, e):.6f}')
    else:
        print('undefined')
    x = round(x + h, 6)
