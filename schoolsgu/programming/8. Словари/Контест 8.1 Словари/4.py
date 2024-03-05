import sys

d = dict()
for s in sys.stdin:
    f = False
    for c in s:
        if c.isalpha():
            c = c.lower()
            d[c] = d.get(c, 0) + 1
        elif c == '.':
            f = True
    if f:
        break
mxc, mxk = '', 0
for c, k in sorted(d.items()):
    if k > mxk:
        mxk = k
        mxc = c
print(mxc, mxk)
