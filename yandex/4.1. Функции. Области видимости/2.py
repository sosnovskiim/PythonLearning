def gcd(n, m):
    while m:
        n, m = m, n % m
    return n


if __name__ == '__main__':
    result = gcd(12, 45)
    print(f'result = {result}')
