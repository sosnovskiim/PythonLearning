n = int(input())
d = dict()
for _ in range(n):
    b, s = input().split(',')
    s = int(s)
    c = s * 0.05
    if b in d:
        d[b] = (d[b][0] + s - c, d[b][1] + c)
    else:
        d[b] = (s - c, c)
a = sorted(d.items(), key=lambda x: (-x[1][0], x[0]))
print('\n'.join(f'{b[0]} {b[1][0]:.2f} {b[1][1]:.2f}' for b in a))
