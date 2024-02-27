n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))
m = int(input())
if sum(a) <= m:
    print('True')
else:
    print('False')
