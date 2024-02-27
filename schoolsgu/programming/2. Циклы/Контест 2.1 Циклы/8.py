n = int(input())
sm, mx = 0, -10 ** 4
for _ in range(n):
    sm += int(input())
    mx = max(mx, sm)
    if sm < 0:
        sm = 0
print(mx)
