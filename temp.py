import sys

base = 131
mod1 = 10 ** 9 + 7
mod2 = 10 ** 9 + 9


def main():
    n = int(sys.stdin.readline().strip())
    s_encrypted = sys.stdin.readline().strip()
    s = s_encrypted[::-1].lower()  # единственный переворот строки
    m = int(sys.stdin.readline().strip())

    # Предподсчет хешей для строки
    n_s = len(s)
    pref1 = [0] * (n_s + 1)
    pref2 = [0] * (n_s + 1)
    pow_base1 = [1] * (n_s + 1)
    pow_base2 = [1] * (n_s + 1)

    for i in range(n_s):
        pref1[i + 1] = (pref1[i] * base + ord(s[i])) % mod1
        pref2[i + 1] = (pref2[i] * base + ord(s[i])) % mod2
        pow_base1[i + 1] = (pow_base1[i] * base) % mod1
        pow_base2[i + 1] = (pow_base2[i] * base) % mod2

    def get_hash(l, r):
        h1 = (pref1[r] - pref1[l] * pow_base1[r - l]) % mod1
        h2 = (pref2[r] - pref2[l] * pow_base2[r - l]) % mod2
        if h1 < 0: h1 += mod1
        if h2 < 0: h2 += mod2
        return (h1, h2)

    words = {}
    for _ in range(m):
        word = sys.stdin.readline().strip()
        low_word = word.lower()  # прямое слово в нижнем регистре
        k = len(low_word)

        # Вычисляем хеш для прямого слова
        h1 = 0
        h2 = 0
        for c in low_word:
            h1 = (h1 * base + ord(c)) % mod1
            h2 = (h2 * base + ord(c)) % mod2

        if k not in words:
            words[k] = {}
        words[k][(h1, h2)] = word  # сохраняем оригинальное слово

    dp = [-1] * (n_s + 1)
    dp[0] = 0  # база ДП

    for i in range(n_s + 1):
        if dp[i] == -1:
            continue
        for k in words:
            j = i + k
            if j > n_s:
                continue

            # Хеш подстроки в перевернутой строке
            h_sub = get_hash(i, j)

            if h_sub in words[k]:
                dp[j] = i  # запоминаем позицию разбиения

    # Восстановление ответа
    res = []
    curr = n_s
    while curr > 0:
        prev = dp[curr]
        k = curr - prev
        h_sub = get_hash(prev, curr)
        word = words[k][h_sub]  # оригинальное слово из словаря
        res.append(word)
        curr = prev

    # Разворачиваем порядок слов
    # res.reverse()
    print(' '.join(res))


if __name__ == "__main__":
    main()