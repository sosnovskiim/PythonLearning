with open('input.txt', 'r') as f1, open('output.txt', 'w') as f2:
    k = int(f1.readline())
    for s in f1.readlines():
        if len(s) > k + 1:
            f2.write(s)
