from itertools import product

n = int(input())
d = list()
for _ in range(n):
    s = set()
    for i in input().split(', '):
        s.add(int(i))
    d.append(s)
for i in sorted(product(*d)):
    print(''.join(str(j) for j in i))
