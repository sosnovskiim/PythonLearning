from collections import defaultdict

d = defaultdict(set)
while s := input():
    for w in s.split():
        d[w[-1].upper()].add(w.lower())
for k, v in d.items():
    print(f'{k} - {", ".join(sorted(v))}')
