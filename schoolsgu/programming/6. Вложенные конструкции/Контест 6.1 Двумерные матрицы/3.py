n, m = map(int, input().split())
k = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(m):
        if data[i][j] > k:
            print(i + 1, j + 1)
