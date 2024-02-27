n = int(input())
for a in range(2, 100):
    t = a ** 3
    if t > n:
        print('No')
        break
    elif t == n:
        for d in range(2, a):
            if a % d == 0:
                break
        else:
            print('Yes')
            break
