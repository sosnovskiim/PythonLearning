n = int(input())
for _ in range(n):
    a, b, s = map(str, input().split('&'))
    a, b = int(a), int(b)
    print(s[a:a + b * 2:2])
