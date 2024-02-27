from math import log
from math import e

a, b, h = map(float, input().split())
x = a
while b - x > 10 ** -6 or abs(x - b) < 10 ** -6:
    print(f'{x:.6f}', end='\t')
    if abs(x - 2) >= 10 ** -6 and x / (x - 2) > 0:
        print(f'{log(x / (x - 2), e):.6f}')
    else:
        print('undefined')
    x += h
