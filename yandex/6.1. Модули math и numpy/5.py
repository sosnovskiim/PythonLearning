from math import cos, sin, dist

x, y = map(float, input().split())
r, f = map(float, input().split())
print(dist((x, y), (r * cos(f), r * sin(f))))
