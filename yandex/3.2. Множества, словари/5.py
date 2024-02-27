n, m = int(input()), int(input())
p = set()
cnt = 0
for _ in range(n + m):
    s = input()
    if s in p:
        cnt += 2
    p.add(s)
if cnt == n + m:
    print('Таких нет')
else:
    print(n + m - cnt)
