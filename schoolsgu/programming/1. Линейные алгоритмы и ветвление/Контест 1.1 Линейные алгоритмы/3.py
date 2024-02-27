n = int(input())
a, b, c = n // 100, n % 100 // 10, n % 10
print(c * 1000 + a * 100 + b * 10 + c)
