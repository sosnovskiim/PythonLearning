with open('input.txt', 'r') as f1, open('output.txt', 'w') as f2:
    k1, k2 = map(int, f1.readline().split())
    cnt = 1
    while cnt <= k2:
        s = f1.readline()
        if cnt >= k1:
            f2.write(s)
        cnt += 1
