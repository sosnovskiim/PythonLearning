def get_pref_suff(len_p, p, s):
    def get_char(i):
        return p[i] if i < len_p + 1 else s[i - len_p - 1]

    n = len_p + len_s + 1
    z = [0] * n
    dp = [inf] * (len_p + 2)
    left, right = 0, 0
    for i in range(1, n):
        if i <= right:
            z[i] = min(z[i - left], right - i + 1)
        while i + z[i] < n and get_char(z[i]) == get_char(i + z[i]):
            z[i] += 1
        if z[i] > 0 and i + z[i] - 1 > right:
            left, right = i, i + z[i] - 1
        if i > len_p and z[i] > 0:
            len_z = min(z[i], len_p)
            if i < dp[len_z]:
                dp[len_z] = i
    for i in range(len_p, 0, -1):
        if dp[i] > dp[i + 1]:
            dp[i] = dp[i + 1]
    return dp


s = input()
len_s = len(s)
rev_s = s[::-1]
inf = 10 ** 9
cnt = 0
for _ in range(int(input())):
    p = input()
    len_p = len(p)
    if len_p < 2:
        continue
    pref = get_pref_suff(len_p, p + "#", s)
    suff = get_pref_suff(len_p, p[::-1] + "#", rev_s)
    f = False
    for i in range(1, len_p):
        if pref[i] == inf or suff[len_p - i] == inf:
            continue
        f = len(s) + len_p - suff[len_p - i] >= pref[i] - 2
        if f:
            break
    if f:
        cnt += 1
print(cnt)
