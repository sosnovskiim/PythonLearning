n = int(input())
p = set()
for _ in range(n):
    p |= set(input().split())
[print(s) for s in p]
