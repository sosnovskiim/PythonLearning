n, m = int(input()), int(input())
p = set()
cnt = 0
for _ in range(n + m):
    s = input()
    if s in p:
        cnt += 1
    p.add(s)
if cnt == 0:
    print('Таких нет')
else:
    print(cnt)
