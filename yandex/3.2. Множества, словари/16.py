a = set()
s = input()
while s:
    p = None
    for c in s.split():
        if p is not None and c == 'зайка':
            a.add(p)
        elif p == 'зайка':
            a.add(c)
        p = c
    s = input()
for t in a:
    print(t)
