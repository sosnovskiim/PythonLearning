from math import log, cos, sin, pi, e

x = float(input())
f = log(x ** (3 / 16), 32) + x ** cos((pi * x) / (2 * e)) - sin(x / pi) ** 2
print(f)
