n = int(input())
a = int(input())
mx = None
for _ in range(n - 1):
    b = int(input())
    if b < a and (mx is None or mx < b):
        mx = b
    a = b
print(mx)
