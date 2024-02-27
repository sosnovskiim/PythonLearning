d = dict()
s = input()
while s:
    for a in s.split():
        d[a] = d.get(a, 0) + 1
    s = input()
for k, v in d.items():
    print(k, v)
