MOD1, MOD2 = 1_000_000_007, 1_000_000_009
P1, P2 = 911_382_323, 972_663_749

MAX_LEN = 600_001
pow1 = [1] * (MAX_LEN + 1)
pow2 = [1] * (MAX_LEN + 1)
for i in range(1, MAX_LEN + 1):
    pow1[i] = (pow1[i - 1] * P1) % MOD1
    pow2[i] = (pow2[i - 1] * P2) % MOD2


def poly_hash(s: str):
    h1 = h2 = 0
    for i, ch in enumerate(s):
        v = ord(ch) - 96
        h1 = (h1 + v * pow1[i]) % MOD1
        h2 = (h2 + v * pow2[i]) % MOD2
    return h1, h2


def solve():
    n, m = map(int, input().split())

    if n == 0:
        for _ in range(m):
            input()
            print("NO")
        return

    hashes = set()

    for _ in range(n):
        s = input().strip()
        hashes.add((*poly_hash(s), len(s)))

    for _ in range(m):
        s = input().strip()
        h1, h2 = poly_hash(s)
        L = len(s)
        found = False

        for i, ch in enumerate(s):
            val_old = ord(ch) - 96
            for ch_new in ('a', 'b', 'c'):
                if ch_new == ch:
                    continue
                val_new = ord(ch_new) - 96
                diff1 = (val_new - val_old) * pow1[i] % MOD1
                diff2 = (val_new - val_old) * pow2[i] % MOD2
                cand = ((h1 + diff1) % MOD1,
                        (h2 + diff2) % MOD2,
                        L)
                if cand in hashes:
                    found = True
                    break
            if found:
                break

        print("YES" if found else "NO")


solve()
