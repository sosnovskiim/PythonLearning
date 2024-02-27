a = [ch.capitalize() for ch in input()]
v = ['A', 'E', 'I', 'O', 'U']
c = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z']
s = ''
for i in range(len(a)):
    if (i == 0 or s[i - 1] == 'C') and a[i] == 'Y' or a[i] in v:
        s += 'V'
    else:
        s += 'C'
print(s)
