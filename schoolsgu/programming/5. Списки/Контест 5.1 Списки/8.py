n = int(input())
a = [int(x) for x in input().split()]
mn, mx = 10 ** 9, -10 ** 9
mni, mxi = 0, 0
for i in range(n):
    if a[i] < mn:
        mn = a[i]
        mni = i
    if a[i] >= mx:
        mx = a[i]
        mxi = i
if mn != mx:
    if mni == 0 and mxi == n - 1 or mxi == 0 and mni == n - 1:
        a = a[::-1]
    elif mni < mxi:
        a[mni:mxi + 1] = a[mxi:mni - 1:-1]
    else:
        a[mxi:mni + 1] = a[mni:mxi - 1:-1]
print(' '.join(map(str, a)))
