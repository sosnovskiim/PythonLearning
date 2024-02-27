from math import log
from math import e

a, b, h = map(float, input().split())
x = a
while b - x > 10 ** -6 or abs(x - b) < 10 ** -6:
    print(f'{x:.6f}', end='\t')
    if abs(x + 7) >= 10 ** -6 and 1 - abs(x) > 0:
        print(f'{1 / (x + 7) + log(1 - abs(x), e):.6f}')
    else:
        print('undefined')
    x += h
