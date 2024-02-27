n = int(input())
s, t = 0, 0
for i in range(n):
    t = t * 2 + i + 1
    s += t
print(s)
