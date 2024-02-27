n = int(input())
d = dict()
for _ in range(n):
    s = input()
    d[s] = d.get(s, 0) + 1
cnt = 0
for s in d.values():
    if s != 1:
        cnt += s
print(cnt)
