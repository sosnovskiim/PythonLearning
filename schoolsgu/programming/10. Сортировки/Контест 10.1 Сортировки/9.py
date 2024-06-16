s = input()
d = dict()
i = 0
while s[i] != '.':
    d[s[i]] = d.get(s[i], 0) + 1
    i += 1
a = sorted(d.items(), key=lambda x: (-x[1], x[0]))
print(''.join(c[0] for c in a))
