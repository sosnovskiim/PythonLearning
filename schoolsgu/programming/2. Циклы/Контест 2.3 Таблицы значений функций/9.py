a, b, h = map(float, input().split())
x = a
while b - x > 10 ** -6 or abs(x - b) < 10 ** -6:
    print(f'{x:.6f}', end='\t')
    if abs(x - 1) >= 10 ** -6 and abs(1 - 4 * x) >= 10 ** -6:
        print(f'{1 / (x - 1) + 2 / (1 - 4 * x):.6f}')
    else:
        print('undefined')
    x += h
