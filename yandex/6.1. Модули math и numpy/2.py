from math import gcd
from sys import stdin

a = [gcd(*[int(x) for x in s.split()]) for s in stdin]
print(*a, sep='\n')
