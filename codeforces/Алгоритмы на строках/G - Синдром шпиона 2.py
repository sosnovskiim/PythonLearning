n = int(input())
s = input()[::-1]
m = int(input())
words = {}
for _ in range(m):
    word = input()
    k = len(word)
    h = hash(word.lower())
    if k not in words:
        words[k] = {}
    words[k][h] = word
dp = [-1] * (n + 1)
dp[0] = 0
for i in range(n + 1):
    if dp[i] == -1:
        continue
    for k in words:
        if i + k > n:
            continue
        h = hash(s[i:i + k])
        if h in words[k]:
            dp[i + k] = i
r = []
curr = n
while curr > 0:
    prev = dp[curr]
    h = hash(s[prev:curr])
    word = words[curr - prev][h]
    r.append(word)
    curr = prev
print(' '.join(r))
