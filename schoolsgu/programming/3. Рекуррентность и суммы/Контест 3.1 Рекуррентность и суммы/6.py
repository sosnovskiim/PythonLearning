a, m = map(int, input().split())
ps, pv = a, a * 1.3
s, v = 0, 0
cnt = 0
while s + v < m:
    cnt += 1
    s, v = s + ps, v + pv
    ps, pv = ps + 6, (ps + 6) * 1.3
print(cnt, s)
