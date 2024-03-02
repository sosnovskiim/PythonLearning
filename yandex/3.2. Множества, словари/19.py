n = int(input())
s1, s2 = set(), set()
for _ in range(n):
    k, v = map(str, input().split(': '))
    for t in set(v.split(', ')):
        if t in s2:
            s1.add(t)
        else:
            s2.add(t)
for t in sorted(s2 - s1):
    print(t)
