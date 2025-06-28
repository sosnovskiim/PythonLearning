def z_func(s):
    z = [0] * len(s)
    left, right = 0, 0
    for i in range(1, len(s)):
        if i <= right:
            z[i] = min(z[i - left], right - i + 1)
        while i + z[i] < len(s) and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if z[i] > 0 and i + z[i] - 1 > right:
            left, right = i, i + z[i] - 1
    return z


s = input()
m = int(input())
words = [input() for _ in range(m)]
inf = 10 ** 9
cnt = 0
for p in words:
    len_p = len(p)
    if len_p < 2:
        continue
    t1 = p + "#" + s
    z1 = z_func(t1)
    pref = [inf] * (len_p + 2)
    for i in range(len_p + 1, len(t1)):
        len_z = z1[i]
        if len_z != 0 and i < pref[len_z]:
            pref[len_z] = i
    for i in range(len_p, 0, -1):
        if pref[i] > pref[i + 1]:
            pref[i] = pref[i + 1]
    t2 = p[::-1] + "#" + s[::-1]
    z2 = z_func(t2)
    suff = [inf] * (len_p + 2)
    for i in range(len_p + 1, len(t2)):
        len_z = z2[i]
        if len_z != 0 and i < suff[len_z]:
            suff[len_z] = i
    for i in range(len_p, 0, -1):
        if suff[i] > suff[i + 1]:
            suff[i] = suff[i + 1]
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
