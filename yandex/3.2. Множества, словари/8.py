n = int(input())
d = dict()
for _ in range(n):
    n, *p = input().split()
    d[n] = p
s = input()
f = True
for k, v in sorted(d.items()):
    if s in v:
        print(k)
        f = False
if f:
    print('Таких нет')
