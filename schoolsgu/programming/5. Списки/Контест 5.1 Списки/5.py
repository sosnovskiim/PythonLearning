n = int(input())
while n >= 10:
    sm = 0
    while n != 0:
        sm += n % 10
        n //= 10
    n = sm
print(n)
