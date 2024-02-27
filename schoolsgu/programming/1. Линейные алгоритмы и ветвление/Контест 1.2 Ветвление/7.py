from math import sqrt

a, b, c, d = int(input()), int(input()), int(input()), int(input())
if min(sqrt(a * a + b * b), sqrt(b * b + c * c), sqrt(a * a + c * c)) <= d:
    print('Yes')
else:
    print('No')
