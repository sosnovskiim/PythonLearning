a, b, h = map(float, input().split())
x = a
while b - x > 10 ** -6 or abs(x - b) < 10 ** -6:
    print(f'{x:.6f}', end='\t')
    d = (1 + x) ** 2
    if abs(d) < 10 ** -6:
        print('undefined')
    else:
        print(f'{1 / d:.6f}')
    x += h
