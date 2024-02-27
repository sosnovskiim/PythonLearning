n = int(input())
cnt = 0
for _ in range(n):
    s = input()
    if s.find('..') == -1 and s.count('@') == 1 and not s.startswith('@') and not s.endswith('@'):
        cnt += 1
print(cnt)
