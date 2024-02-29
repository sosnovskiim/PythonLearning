d = dict()
s = input()
while s:
    p, f = map(str, s.split())
    d[p] = d.get(p, []) + [f]
    s = input()
print(d)
