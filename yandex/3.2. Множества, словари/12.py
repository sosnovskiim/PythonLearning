n = int(input())
d = dict()
for _ in range(n):
    s = input()
    d[s] = d.get(s, 0) + 1
f = True
for k, v in sorted(d.items()):
    if v != 1:
        print(f'{k} - {v}')
        f = False
if f:
    print('Однофамильцев нет')
