s = input()
d = {'2': 0, '3': 0, '4': 0, '5': 0}
i = 0
while i < len(s):
    if s[i] == '0':
        d['2'] += 1
        i += 1
    elif s[i + 1] == '1':
        d['5'] += 1
        i += 2
    elif s[i + 2] == '0':
        d['3'] += 1
        i += 3
    else:
        d['4'] += 1
        i += 3
mxk, mxv = '', 0
for k, v in d.items():
    if v > mxv:
        mxv = v
        mxk = k
print(mxk)
