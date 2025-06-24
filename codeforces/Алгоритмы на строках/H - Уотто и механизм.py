def hash_abc(s: str, a: dict[str, int], b: list[int], p: int) -> int:
    h = 0
    for i in range(len(s)):
        h += (a[s[i]] * b[i]) % p
    return h


n, m = map(int, input().split())
a = {"a": ord("a"), "b": ord("b"), "c": ord("c")}
b = [1] * 10 ** 6
p = 10 ** 9 + 7
for i in range(1, len(b)):
    b[i] = (5 * b[i - 1]) % p
t = {hash_abc(input(), a, b, p) for _ in range(n)}
r = ""
for _ in range(m):
    s = input()
    # h = hash_abc(s, a, b, p)
    f = False
    for i in range(len(s)):
        # h_old = (a[s[i]] * b[i]) % p
        # h -= h_old
        for c in a.keys():
            if c != s[i]:
                h = hash_abc(s[:i] + c + s[i + 1:], a, b, p)
                # h_new = (a[c] * b[i]) % p
                # h += h_new
                f = h in t
                # h -= h_new
                if f:
                    break
        # h += h_old
        if f:
            r += "YES\n"
            break
    else:
        r += "NO\n"
print(r)
