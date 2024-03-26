def recursive_digit_sum(n):
    if __name__ == '__main__':
        print(f'# Вызов recursive_digit_sum({n})')
    if n == 0:
        return 0
    return recursive_digit_sum(n // 10) + n % 10


if __name__ == '__main__':
    result = recursive_digit_sum(123)
    print(f'result = {result}')
