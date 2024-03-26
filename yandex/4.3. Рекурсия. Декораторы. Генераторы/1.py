def recursive_sum(*numbers):
    if __name__ == '__main__':
        print(f'# Вызов recursive_sum({", ".join(map(str, numbers))})')
    if len(numbers) == 0:
        return 0
    return recursive_sum(*numbers[:len(numbers) - 1]) + numbers[-1]


if __name__ == '__main__':
    result = recursive_sum(1, 2, 3)
    print(f'result = {result}')
