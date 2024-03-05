from collections import defaultdict

d = defaultdict(set)
while s := input():
    p, f = map(str, s.split())
    d[p].add(f)
    d[f].add(p)
for p in sorted(d):
    s = set()
    for f in d[p]:
        for ff in d[f]:
            if ff != p and ff not in d[p]:
                s.add(ff)
    print(f'{p}: {", ".join(sorted(s))}')
