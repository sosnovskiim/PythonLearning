s = input()
p = [0] * len(s)
cnt = {i: 0 for i in range(len(s) + 1)}
cnt[0] = 1
for i in range(1, len(s)):
    k = p[i - 1]
    while k and s[k] != s[i]:
        k = p[k - 1]
    if s[k] == s[i]:
        k += 1
    p[i] = k
    cnt[k] += 1
ans = []
k = len(s)
while k != 0:
    ans.append(k)
    k = p[k - 1]
for i in range(len(s) - 1, 0, -1):
    if p[i] != -1:
        cnt[p[i - 1]] += cnt[i]
print(len(ans))
for i in ans[::-1]:
    print(i, cnt[i] + 1)
