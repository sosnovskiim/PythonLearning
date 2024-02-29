a = list()
for n in input().split():
    b = bin(int(n))[2:]
    d = {'digits': 0, 'units': 0, 'zeros': 0}
    for t in b:
        d['digits'] += 1
        if t == '1':
            d['units'] += 1
        else:
            d['zeros'] += 1
    a.append(d)
print(a)
