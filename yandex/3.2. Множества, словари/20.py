from collections import defaultdict
from math import sqrt

d = defaultdict(set)
for n in map(int, input().split('; ')):
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            d[n].add(i)
            if i != n // i:
                d[n].add(n // i)
for k, v in sorted(d.items()):
    s = set()
    for i in d.keys():
        if len(v & d[i]) == 1:
            s.add(i)
    if s:
        print(f'{k} - {", ".join(str(i) for i in sorted(s))}')
