def fibonacci(n):
    n1, n2 = 0, 1
    for i in range(n):
        yield n1
        n1, n2 = n2, n1 + n2


if __name__ == '__main__':
    print(*fibonacci(10), sep=', ')
