from math import prod

a = [float(x) for x in input().split()]
g = prod(a) ** (1 / len(a))
print(g)
