n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(m // 2):
        data[i][j], data[i][m - j - 1] = data[i][m - j - 1], data[i][j]
for line in data:
    print(' '.join(map(str, line)))
