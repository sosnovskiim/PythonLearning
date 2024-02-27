n = int(input())
mx, mxi = 0, 0
for i in range(n):
    t = abs(int(input()))
    if t >= mx:
        mx, mxi = t, i + 1
print(mxi)
