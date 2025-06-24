n, w = map(int, input().split())
a = [int(x) for x in input().split()]
b = [int(y) for y in input().split()]
if w == 1:
    print(n)
    exit()
c, d = [], []
for i in range(n - 1):
    c.append(a[i + 1] - a[i])
for i in range(w - 1):
    d.append(b[i + 1] - b[i])
p = [0] * (w - 1)
for i in range(1, w - 1):
    k = p[i - 1]
    while k > 0 and d[k] != d[i]:
        k = p[k - 1]
    if d[k] == d[i]:
        k += 1
    p[i] = k
i, j, k = 0, 0, 0
while i < n - 1:
    if c[i] == d[j]:
        i += 1
        j += 1
    if j == w - 1:
        k += 1
        j = p[j - 1]
    elif i < n - 1 and c[i] != d[j]:
        if j != 0:
            j = p[j - 1]
        else:
            i += 1
print(k)
