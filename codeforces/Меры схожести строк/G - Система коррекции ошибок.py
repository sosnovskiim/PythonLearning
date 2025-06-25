from collections import defaultdict


def hamming(s: list[str], t: str) -> int:
    d = 0
    for c1, c2 in zip(s, t):
        if c1 != c2:
            d += 1
    return d


n = int(input())
s = list(input())
t = input()
base = hamming(s, t)
if base == 0:
    print(0)
    print(-1, -1)
    exit()
pos = defaultdict(list)
for i in range(n):
    pos[s[i]].append(i)
for i in range(n):
    if s[i] != t[i]:
        for j in pos.get(t[i], []):
            s[i], s[j] = s[j], s[i]
            print(hamming(s, t))
            print(i + 1, j + 1)
            exit()
print(base)
print(-1, -1)
