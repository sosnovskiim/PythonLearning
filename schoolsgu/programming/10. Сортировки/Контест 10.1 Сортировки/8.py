n = int(input())
a = [input().split() for _ in range(n)]
o = input()
a.sort(key=lambda x: int(x[0]))
b, c, k, p = [], [], [], []
for s in a:
    if s[1] == 'b':
        b.append(s[0])
    elif s[1] == 'c':
        c.append(s[0])
    elif s[1] == 'k':
        k.append(s[0])
    else:
        p.append(s[0])
for s in o:
    if s == 'b':
        print(f'b: {" ".join(b)}')
    elif s == 'c':
        print(f'c: {" ".join(c)}')
    elif s == 'k':
        print(f'k: {" ".join(k)}')
    else:
        print(f'p: {" ".join(p)}')
