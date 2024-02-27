n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
sm, cnt = 0, 0
for i in range(n):
    for j in range(n - i, n):
        sm += data[i][j]
        cnt += 1
if cnt == 0:
    print('No')
else:
    print(f'{sm / cnt:.6f}')
