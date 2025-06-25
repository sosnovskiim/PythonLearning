s1, s2 = input(), input()
n, m = len(s1), len(s2)
dp = [[0] * (m + 1) for _ in range(n + 1)]
ord_a = ord("a")
for i in range(1, n + 1):
    dp[i][0] = dp[i - 1][0] + (ord(s1[i - 1]) - ord_a + 1)
for j in range(1, m + 1):
    dp[0][j] = dp[0][j - 1] + (ord(s2[j - 1]) - ord_a + 1)
for i in range(1, n + 1):
    for j in range(1, m + 1):
        c1, c2 = s1[i - 1], s2[j - 1]
        if c1 != c2:
            add = dp[i][j - 1] + ord(c2) - ord_a + 1
            delete = dp[i - 1][j] + ord(c1) - ord_a + 1
            change = dp[i - 1][j - 1] + abs(ord(c1) - ord(c2))
            dp[i][j] = min(add, delete, change)
        else:
            dp[i][j] = dp[i - 1][j - 1]
print(dp[n][m])
