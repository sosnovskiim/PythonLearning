import sys
from collections import defaultdict

def main():
    n, m = map(int, input().split())

    # Два разных основания и модуля
    base1 = 911382629
    base2 = 3571428571
    mod1 = 10**18 + 3
    mod2 = 10**18 + 7

    # Предподсчет степеней
    max_len = 6 * 10**5 + 10
    pow1 = [1] * max_len
    pow2 = [1] * max_len
    for i in range(1, max_len):
        pow1[i] = (pow1[i-1] * base1) % mod1
        pow2[i] = (pow2[i-1] * base2) % mod2

    mechanism = set()

    for _ in range(n):
        s = input()
        h1 = h2 = 0
        for c in s:
            h1 = (h1 * base1 + ord(c)) % mod1
            h2 = (h2 * base2 + ord(c)) % mod2
        mechanism.add((h1, h2))

    result = []
    for _ in range(m):
        s = input()
        L = len(s)
        h1 = h2 = 0
        for c in s:
            h1 = (h1 * base1 + ord(c)) % mod1
            h2 = (h2 * base2 + ord(c)) % mod2

        found = False
        for i in range(L):
            # Удаляем вклад текущего символа
            temp_h1 = (h1 - ord(s[i]) * pow1[L-i-1]) % mod1
            temp_h2 = (h2 - ord(s[i]) * pow2[L-i-1]) % mod2
            # Пробуем заменить на другие символы
            for c in 'abc':
                if c == s[i]:
                    continue
                new_h1 = (temp_h1 + ord(c) * pow1[L-i-1]) % mod1
                new_h2 = (temp_h2 + ord(c) * pow2[L-i-1]) % mod2
                if (new_h1, new_h2) in mechanism:
                    found = True
                    break
            if found:
                break
        result.append("YES" if found else "NO")

    print('\n'.join(result))

if __name__ == "__main__":
    main()