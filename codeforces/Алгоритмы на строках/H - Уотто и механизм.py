def hash_abc(s: str) -> (int, int):
    h1 = h2 = 0
    for c in s:
        h1 = (h1 * b1 + ord(c)) % p1
        h2 = (h2 * b2 + ord(c)) % p2
    return h1, h2


n, m = map(int, input().split())
b1 = 911382629
b2 = 972663749
p1 = 10 ** 9 + 7
p2 = 10 ** 9 + 9
max_len = 6 * 10 ** 5 + 1
pow1 = [1] * max_len
pow2 = [1] * max_len
for i in range(1, max_len):
    pow1[i] = (pow1[i - 1] * b1) % p1
    pow2[i] = (pow2[i - 1] * b2) % p2
t = {hash_abc(input()) for _ in range(n)}
r = []
for _ in range(m):
    s = input()
    ln = len(s)
    h1, h2 = hash_abc(s)
    f = False
    for i in range(ln):
        h_old_1 = (h1 - ord(s[i]) * pow1[ln - i - 1]) % p1
        h_old_2 = (h2 - ord(s[i]) * pow2[ln - i - 1]) % p2
        for c in ("a", "b", "c"):
            if c != s[i]:
                h_new_1 = (h_old_1 + ord(c) * pow1[ln - i - 1]) % p1
                h_new_2 = (h_old_2 + ord(c) * pow2[ln - i - 1]) % p2
                f = (h_new_1, h_new_2) in t
                if f:
                    break
        if f:
            break
    r.append("YES" if f else "NO")
print('\n'.join(r))
