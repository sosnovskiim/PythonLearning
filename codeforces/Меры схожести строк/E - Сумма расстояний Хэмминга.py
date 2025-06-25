a, b = input(), input()
n, m = len(a), len(b)
p0 = [0] * (m + 1)
p1 = [0] * (m + 1)
for i in range(1, m + 1):
    p0[i] = p0[i - 1] + int(b[i - 1] == "0")
    p1[i] = p1[i - 1] + int(b[i - 1] == "1")
d = 0
for i in range(n):
    left = i
    right = m - n + i + 1
    if a[i] == "0":
        d += p1[right] - p1[left]
    else:
        d += p0[right] - p0[left]
print(d)
