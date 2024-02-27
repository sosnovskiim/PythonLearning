s = input()
r = 0
for c in s:
    if c.isdigit():
        r += int(c)
print(r)
