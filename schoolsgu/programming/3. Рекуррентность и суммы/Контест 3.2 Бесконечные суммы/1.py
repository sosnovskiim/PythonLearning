h, e = map(float, input().split())
x = 0.2
while x - 1.8 < 1e-9:
    y = x
    n, sm = 0, 0
    while y - e > 1e-9:
        if n == 10000:
            sm = 0
            break
        n += 1
        sm += y
        y = (x * y ** 2 + 2 * y) / 13
    print(f'{x:.8f} {sm:.8f}')
    x += h
