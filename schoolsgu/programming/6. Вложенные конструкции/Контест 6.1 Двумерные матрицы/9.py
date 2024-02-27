n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
if n % 2 == 0:
    for i in range(0, n, 2):
        data[i], data[i + 1] = data[i + 1], data[i]
for line in data:
    print(' '.join(map(str, line)))
