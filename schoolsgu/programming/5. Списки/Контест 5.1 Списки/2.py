n = int(input())
a = [int(x) for x in input().split()]
mx, mxi = -100000, 0
for i in range(n):
    if a[i] > mx:
        mx = a[i]
        mxi = i
a[mxi] *= -1
print(' '.join(map(str, a)))
