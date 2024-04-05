n, m = int(input()), int(input())
p, t = set(), set()
for _ in range(n + m):
    s = input()
    if s in p:
        t.add(s)
    p.add(s)
if len(p) == len(t):
    print('Таких нет')
else:
    [print(s) for s in sorted(p - t)]
