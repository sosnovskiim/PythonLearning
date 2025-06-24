def hash_abc_string(s: str, a: dict[str, int], b: int, p: int) -> int:
    h = 0
    for i in range(len(s)):
        h += a[s[i]] * b ** (len(s) - i - 1)
    return h % p


def hash_abc_char(c: str, pow: int, a: dict[str, int], b: int, p: int) -> int:
    return (a[c] * b ** pow) % p


def is_hash_exists(a: list[int], h: int) -> bool:
    left, right = 0, len(a) - 1
    while left <= right:
        mid = (left + right) // 2
        if a[mid] == h:
            return True
        elif a[mid] < h:
            left = mid + 1
        else:
            right = mid - 1
    return False


n, m = map(int, input().split())
a = {"a": ord("a"), "b": ord("b"), "c": ord("c")}
b = 3
p = 10 ** 9 + 7
memory = {hash_abc_string(input(), a, b, p) for _ in range(n)}
# memory.sort()
r = ""
for _ in range(m):
    s = input()
    h = hash_abc_string(s, a, b, p)
    f = False
    for i in range(len(s)):
        pow = len(s) - i - 1
        h_old = hash_abc_char(s[i], pow, a, b, p)
        for c in ("a", "b", "c"):
            if c != s[i]:
                h_new = hash_abc_char(c, pow, a, b, p)
                # f = is_hash_exists(memory, h - h_old + h_new)
                f = (h - h_old + h_new) in memory
                if f:
                    break
        if f:
            r += "YES\n"
            break
    else:
        r += "NO\n"
print(r)
