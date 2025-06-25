s, t = input(), input()
n = len(s)
cnt = 0
for i in range(n):
    if s[i] != t[i]:
        cnt += 1
if cnt % 2 != 0:
    print("impossible")
    exit()
b = True
for i in range(n):
    if s[i] != t[i]:
        if b:
            print(s[i], end='')
        else:
            print(t[i], end='')
        b = not b
    else:
        print(s[i], end='')
