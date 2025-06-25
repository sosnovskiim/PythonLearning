n, k = map(int, input().split())
s = [ord(c) for c in input()]
ord_a, ord_z = ord("a"), ord("z")
for i in range(n):
    d1 = abs(s[i] - ord_a)
    d2 = abs(s[i] - ord_z)
    if d1 > d2:
        v = min(d1, k)
        s[i] -= v
        k -= v
    else:
        v = min(d2, k)
        s[i] += v
        k -= v
if k > 0:
    print(-1)
else:
    print(''.join(map(chr, s)))
