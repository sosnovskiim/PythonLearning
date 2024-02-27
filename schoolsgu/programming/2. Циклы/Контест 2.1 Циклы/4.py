n = int(input())
mx = 1
p = 0
cnt = 0
for _ in range(n):
    t = int(input())
    if t != p:
        if cnt > mx:
            mx = cnt
        cnt = 1
        p = t
    else:
        cnt += 1
if cnt > mx:
    mx = cnt
print(mx)
