n, m, k = map(int, input().split())
a = [int(x) for x in input().split()]
sm = 0
for x in a:
    if abs(x) % 10 == k and x % m != 0:
        sm += x
print(sm)
