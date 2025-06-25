from math import gcd

n, m = map(int, input().split())
x, y = input(), input()
len_x, len_y = len(x), len(y)
len_gcd = gcd(len_x, len_y)
len_lcm = (len_x * len_y) // len_gcd
r = len_lcm
for j in range(len_gcd):
    cnt = {}
    for i in range(j, len_y, len_gcd):
        cnt[y[i]] = cnt.get(y[i], 0) + 1
    for i in range(j, len_x, len_gcd):
        r -= cnt.get(x[i], 0)
r *= (n * len_x) // len_lcm
print(r)
