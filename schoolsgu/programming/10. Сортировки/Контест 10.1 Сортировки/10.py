n = int(input())
d = dict()
for _ in range(n):
    c = input()
    d[c] = d.get(c, 0) + 1
a = sorted(d.items(), key=lambda x: (-x[1], x[0]))
print('\n'.join(f'{c[0]} {c[1]}' for c in a))
