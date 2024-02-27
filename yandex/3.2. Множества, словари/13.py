n = int(input())
d = {input() for _ in range(n)}
m = int(input())
p = set()
for _ in range(m):
    t = int(input())
    [p.add(input()) for _ in range(t)]
if len(d) == len(p):
    print('Готовить нечего')
else:
    [print(s) for s in sorted(d - p)]
