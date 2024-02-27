n = int(input())
n1, n2 = 1, 3
cnt = 1
while n2 <= n:
    n1, n2 = n2, (n1 + n2) // 2 + 2
    cnt += 1
print(cnt)
