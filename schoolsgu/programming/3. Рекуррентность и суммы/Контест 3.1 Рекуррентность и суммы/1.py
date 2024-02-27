k = int(input())
f1, f2 = 0, 1
for _ in range(k):
    f1, f2 = f2, f2 + f1
print(f1)
