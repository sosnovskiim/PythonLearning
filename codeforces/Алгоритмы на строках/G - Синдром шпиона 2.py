def get_hash(left, right):
    h1 = (pref1[right] - pref1[left] * pow1[right - left]) % p1
    h2 = (pref2[right] - pref2[left] * pow2[right - left]) % p2
    if h1 < 0:
        h1 += p1
    if h2 < 0:
        h2 += p2
    return h1, h2


n = int(input())
s = input()[::-1]
m = int(input())
pref1 = [0] * (n + 1)
pref2 = [0] * (n + 1)
pow1 = [1] * (n + 1)
pow2 = [1] * (n + 1)
b = 131
p1 = 10 ** 9 + 7
p2 = 10 ** 9 + 9
for i in range(n):
    pref1[i + 1] = (pref1[i] * b + ord(s[i])) % p1
    pref2[i + 1] = (pref2[i] * b + ord(s[i])) % p2
    pow1[i + 1] = (pow1[i] * b) % p1
    pow2[i + 1] = (pow2[i] * b) % p2
words = {}
for _ in range(m):
    word = input()
    word_low = word.lower()
    k = len(word)
    h1 = h2 = 0
    for c in word_low:
        h1 = (h1 * b + ord(c)) % p1
        h2 = (h2 * b + ord(c)) % p2
    if k not in words:
        words[k] = {}
    words[k][(h1, h2)] = word
dp = [-1] * (n + 1)
dp[0] = 0
for i in range(n + 1):
    if dp[i] == -1:
        continue
    for k in words:
        j = i + k
        if j > n:
            continue
        h = get_hash(i, j)
        if h in words[k]:
            dp[j] = i
r = []
curr = n
while curr > 0:
    prev = dp[curr]
    h = get_hash(prev, curr)
    word = words[curr - prev][h]
    r.append(word)
    curr = prev
print(' '.join(r))
