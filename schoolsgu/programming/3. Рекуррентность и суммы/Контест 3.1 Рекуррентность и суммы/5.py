a, n = map(int, input().split())
b, pb, g, pg = a, a, a // 2, a // 2
cnt = 1
while b + g < n:
    pb, pg = int(pb * 0.9), int(pg * 1.15)
    if pb + pg == 0:
        cnt = 0
        break
    b, g = b + pb, g + pg
    cnt += 1
print(cnt, b, g)
