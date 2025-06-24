s = input()
n = len(s)
p = [0] * n
cnt = {i: 0 for i in range(n + 1)}
cnt[0] = 1
for i in range(1, n):
    k = p[i - 1]
    while k > 0 and s[k] != s[i]:
        k = p[k - 1]
    if s[k] == s[i]:
        k += 1
    p[i] = k
    cnt[k] += 1
if p[n - 1] > 0 and cnt[p[n - 1]] > 1:
    print(s[:p[n - 1]])
elif p[n - 1] > 0 and p[p[n - 1] - 1] > 0:
    print(s[:p[p[n - 1] - 1]])
else:
    print("Just a legend")
