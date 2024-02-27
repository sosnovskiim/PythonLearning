a = [w for w in input().split()]
s = ''
for w in a:
    for c in w:
        if c.isalpha():
            s += c.capitalize()
if s == s[::-1]:
    print('Yes')
else:
    print('No')
