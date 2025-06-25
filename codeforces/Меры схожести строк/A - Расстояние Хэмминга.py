s1, s2 = input(), input()
d = 0
for c1, c2 in zip(s1, s2):
    if c1 != c2:
        d += 1
print(d)
