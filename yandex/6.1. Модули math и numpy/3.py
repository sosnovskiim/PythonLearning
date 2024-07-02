from math import comb

n, m = map(int, input().split())
c = comb(n, m)
print(c * m // n, c)
