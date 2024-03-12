def gcd(n, m):
    while m:
        n, m = m, n % m
    return n
