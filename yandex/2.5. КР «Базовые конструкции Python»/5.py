n = int(input())
mx = None
for _ in range(n):
    s = input()
    sm, cnt = 0, 0
    while s != 'next':
        sm += int(s)
        cnt += 1
        s = input()
    a = sm / cnt
    if mx is None or mx < a:
        mx = a
print(f'{mx:.2f}')
