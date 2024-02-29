s = input()
d = dict()
for c in s:
    if c not in d:
        d[c] = 0
    d[c] += 1
print(d)

d1 = dict()
for c in s:
    d1[c] = d1.get(c, 0) + 1
print(d1)
print(d1.keys())
print(d1.values())
print(d1.items())
for x in d1:
    print(x, d1[x])
for x, y in sorted(d1.items()):
    print(x, y)
d1.clear()
print(d1)

d2 = dict()
d2['k'] = d2.setdefault('k', []).append('v')
print(d2)

from collections import defaultdict

d3 = defaultdict(list)
d3['k'].append('v')
print(d3)

d4 = {'A': '-.-.',
      'B': '--.'}
print(d4)

import sys
text = sys.stdin.read()
