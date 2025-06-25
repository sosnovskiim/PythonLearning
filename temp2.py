def hash_abc(s: str) -> int:
    h = 0
    for i, c in enumerate(s):
        o = ord(c) - 96
        h = (h + o * b[i]) % p
    return h


n, m = map(int, input().split())
mod = 911_382_323
p = 10 ** 9 + 7
b = [1] * 10 ** 6
for i in range(1, len(b)):
    b[i] = (mod * b[i - 1]) % p
t = {hash_abc(input()) for _ in range(n)}
r = ""
for _ in range(m):
    s = input()
    h = hash_abc(s)
    f = False
    for i, c1 in enumerate(s):
        o1 = ord(c1) - 96
        for c2 in ("a", "b", "c"):
            if c2 != c1:
                o2 = ord(c2) - 96
                d = (o2 - o1) * b[i] % p
                h = (h + d) % p
                f = h in t
                if f:
                    break
        if f:
            break
    r += "YES\n" if f else "NO\n"
print(r)
