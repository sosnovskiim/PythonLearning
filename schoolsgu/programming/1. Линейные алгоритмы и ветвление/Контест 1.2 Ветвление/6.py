n, m, x, y = int(input()), int(input()), int(input()), int(input())
n, m = max(n, m), min(n, m)
print(min(x, n - y, y, m - x))
