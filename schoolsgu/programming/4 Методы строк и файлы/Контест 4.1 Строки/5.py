s = input()
k = len(s)
if k % 2 == 0:
    s = s[:k // 2 - 1] + s[k // 2 + 1:]
else:
    s = s[:k // 2] + s[k // 2 + 1:]
print(s)
