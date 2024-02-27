a, b, h = map(float, input().split())
x = a
while b - x > 10 ** -6 or abs(x - b) < 10 ** -6:
    print(f'{x:.6f}', end='\t')
    t = x ** 3 + 8
    if abs(t) >= 10 ** -6:
        print(f'{3 / abs(t):.6f}')
    else:
        print('undefined')
    x += h
