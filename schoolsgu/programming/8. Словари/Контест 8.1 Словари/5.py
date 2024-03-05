d1, d2 = dict(), dict()
for c in input():
    d1[c] = d1.get(c, 0) + 1
for c in input():
    d2[c] = d2.get(c, 0) + 1
for c in d2:
    if c not in d1 or d2[c] > d1[c]:
        print(False)
        break
else:
    print(True)
