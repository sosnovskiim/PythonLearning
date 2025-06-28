import sys

s = sys.stdin.readline().strip()
t = sys.stdin.readline().strip()
n, m = len(s), len(t)
p = [0] * m
for i in range(1, m):
    k = p[i - 1]
    while k > 0 and t[k] != t[i]:
        k = p[k - 1]
    if t[k] == t[i]:
        k += 1
    p[i] = k
dp = [[0] * 26 for _ in range(m)]
for j in range(m):
    for k in range(26):
        c = chr(ord("a") + k)
        if j > 0 and c != t[j]:
            dp[j][k] = dp[p[j - 1]][k]
        else:
            dp[j][k] = j + (1 if c == t[j] else 0)
dp_prev = [-1] * m
dp_prev[0] = 0
st_curr = {0}
for i in range(n):
    dp_next = [-1] * m
    st_next = set()
    if s[i] == "?":
        chars = [chr(ord("a") + j) for j in range(26)]
    else:
        chars = [s[i]]
    for j in st_curr:
        for c in chars:
            k = ord(c) - ord("a")
            st = dp[j][k]
            add = 0
            if st == m:
                add = 1
                st = p[m - 1]
            new = dp_prev[j] + add
            if new > dp_next[st]:
                dp_next[st] = new
                st_next.add(st)
    dp_prev = dp_next
    st_curr = st_next
print(max(dp_prev))
