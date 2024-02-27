v1, m1, v2, m2 = int(input()), int(input()), int(input()), int(input())
p1, p2 = m1 / v1, m2 / v2
if p1 > p2:
    print('1')
elif p2 > p1:
    print('2')
else:
    print('=')
