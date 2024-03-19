from functools import reduce


def gcd(*args):
    return reduce(lambda x, y: f(x, y), args)


def f(n, m):
    while m:
        n, m = m, n % m
    return n


if __name__ == '__main__':
    result = gcd(3)
    print(f'result = {result}')
