n = int(input())
d = dict()
for _ in range(n):
    x, y = map(str, input().split())
    k = f'{x[:-1]} {y[:-1]}'
    d[k] = d.get(k, 0) + 1
print(max(d.values()))
