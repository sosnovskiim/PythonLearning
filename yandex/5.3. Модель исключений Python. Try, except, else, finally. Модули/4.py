def only_positive_even_sum(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError
    a, b = int(a), int(b)
    if a <= 0 or a % 2 != 0 or b <= 0 or b % 2 != 0:
        raise ValueError
    return a + b


if __name__ == '__main__':
    print(only_positive_even_sum(-5, 4))
