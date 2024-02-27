h, e = map(float, input().split())
x = 0.2
while x - 0.8 < 1e-9:
    y1, y2 = 1, x
    n, sm = 0, y1
    while y2 - e > 1e-9:
        if n == 10000:
            sm = 0
            break
        n += 1
        sm += y2
        y1, y2 = y2, ((x ** 2 - 2) * y2) / ((x ** 2 - 1) * (n ** 2)) + ((y1 ** 2) / (n ** 2))
    print(f'{x:.8f} {sm:.8f}')
    x += h
