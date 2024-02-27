a, b = map(int, input().split())
mxd, ans = 0, 0
for n in range(a, b + 1):
    cnt = 0
    for d in range(2, n // 2 + 1):
        if n % d == 0:
            cnt += 1
    if cnt >= mxd:
        mxd = cnt
        ans = n
print(ans)
