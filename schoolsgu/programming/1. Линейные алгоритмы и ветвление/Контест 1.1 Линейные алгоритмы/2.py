n = int(input())
a, b, c = n // 100, n % 100 // 10, n % 10
print(a + b + c, a * b * c, sep='\n')
