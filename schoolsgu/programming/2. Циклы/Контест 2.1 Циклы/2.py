p = 1
for _ in range(20):
    t = float(input())
    if t < 0:
        break
    else:
        p *= t
print(format(p, '.6f'))
