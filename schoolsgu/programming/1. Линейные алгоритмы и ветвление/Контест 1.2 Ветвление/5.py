x1, x2, x3 = map(int, input().split())
if abs(x1 - x2) < abs(x1 - x3):
    print(abs(x1 - x2) + abs(x2 - x3))
else:
    print(abs(x1 - x3) + abs(x3 - x2))
