n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
for j in range(m):
    mn = 1_000_000
    for i in range(n):
        if data[i][j] < mn:
            mn = data[i][j]
    print(mn, end=' ')
