from math import sqrt

n = int(input())
cnt = 0
for d in range(2, n // 2 + 1):
    if n % d == 0:
        for t in range(2, int(sqrt(d)) + 1):
            if d % t == 0:
                break
        else:
            k = n // d
            for t in range(2, int(sqrt(k)) + 1):
                if k % t == 0:
                    break
            else:
                print('Yes')
                break
else:
    print('No')
