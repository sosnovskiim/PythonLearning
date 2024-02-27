n = int(input())
p = {input() for _ in range(n)}
m = int(input())
d = set()
for _ in range(m):
    s = input()
    t = int(input())
    f = True
    for _ in range(t):
        if input() not in p:
            f = False
    if f:
        d.add(s)
if len(d) == 0:
    print('Готовить нечего')
else:
    [print(s) for s in sorted(d)]
