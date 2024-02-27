n = int(input())
n1, n2 = 0, 0.1
for _ in range(n):
    n1, n2 = n2, n2 + n1
print(round(n1, 1))
