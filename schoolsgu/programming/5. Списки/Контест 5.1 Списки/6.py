n, m = map(int, input().split())
a, b = [int(x) for x in input().split()], [int(x) for x in input().split()]
c = []
i, j = 0, 0
while i < n and j < m:
    if a[i] <= b[j]:
        c.append(a[i])
        i += 1
    else:
        c.append(b[j])
        j += 1
c += a[i:] + b[j:]
print(' '.join(map(str, c)))
