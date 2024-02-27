n = int(input())
d = dict()
for _ in range(n):
    a = input().split()
    d[a[0]] = a[1:]
s = input()
f = True
for k, v in sorted(d.items()):
    if s in v:
        print(k)
        f = False
if f:
    print('Таких нет')
