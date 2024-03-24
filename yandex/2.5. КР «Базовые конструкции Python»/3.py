m, n = int(input()), int(input())
print(', '.join(list(str(i) for i in range(n, m + 1, (n - m) % 10))))
