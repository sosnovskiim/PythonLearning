a, b = map(int, input().split())
k = 0
cnt = 0
r1, r2 = None, None
while a < b or k < 1_000_000:
    cnt += 1
    if r1 is None and a >= b:
        r1 = cnt
    k += a
    if r2 is None and k >= 1_000_000:
        r2 = cnt
    a *= 3
print(r1, r2)
