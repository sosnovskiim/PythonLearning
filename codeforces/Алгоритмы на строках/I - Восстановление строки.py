for _ in range(int(input())):
    n = int(input())
    p = [int(x) for x in input().split()]
    s = [0] * n
    d = 0
    for i in range(n):
        if p[i] == 0:
            s[i] = d
            d += 1
        else:
            s[i] = s[p[i] - 1]
    print(' '.join(map(str, s)))
