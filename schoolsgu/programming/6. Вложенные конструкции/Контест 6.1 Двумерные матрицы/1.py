n, m = map(int, input().split())
a, b = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(m):
        if a <= data[i][j] <= b:
            data[i][j] = 0
for line in data:
    print(' '.join(map(str, line)))
