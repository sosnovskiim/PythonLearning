n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
sm, cnt = 0, 0
for i in range(n):
    for j in range(m):
        sm += data[i][j]
        cnt += 1
print(f'{sm / cnt:.6f}')
