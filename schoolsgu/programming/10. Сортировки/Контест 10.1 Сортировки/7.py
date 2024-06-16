n = int(input())
a = [input().split() for _ in range(n)]
e = input()
a.sort(key=lambda x: int(x[2]), reverse=True)
a.sort(key=lambda x: x[0])
i, cnt = 0, 0
while i < len(a) and cnt < 10:
    if a[i][1] != e:
        print(' '.join(a[i]))
        cnt += 1
    i += 1
