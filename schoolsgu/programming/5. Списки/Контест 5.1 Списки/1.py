n = int(input())
a = [int(input()) for _ in range(n)]
k = int(input())
a = [x * k for x in a]
print(' '.join(map(str, a)))
