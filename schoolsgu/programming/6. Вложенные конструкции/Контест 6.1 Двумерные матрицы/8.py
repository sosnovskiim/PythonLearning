n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
if n % 2 == 0:
    data[n // 2], data[n // 2 - 1] = data[n // 2 - 1], data[n // 2]
else:
    data[n // 2], data[0] = data[0], data[n // 2]
for line in data:
    print(' '.join(map(str, line)))
