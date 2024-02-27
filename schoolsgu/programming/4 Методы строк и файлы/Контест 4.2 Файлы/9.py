with open('input.txt', 'r') as f1, open('output.txt', 'w') as f2:
    k1, k2 = map(int, f1.readline().split())
    for s in f1.readlines():
        f2.write(s[k1 - 1:k2] + '\n')
