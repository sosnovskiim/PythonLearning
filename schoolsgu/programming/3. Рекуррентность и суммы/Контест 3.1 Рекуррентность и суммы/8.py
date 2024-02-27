s, k, m = map(int, input().split())
cnt = 0
while s - k >= 0:
    cnt += 1
    s -= k
    s += m
print(cnt)
