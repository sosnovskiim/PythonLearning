def split_numbers(numbers):
    return tuple(int(i) for i in numbers.split())


if __name__ == '__main__':
    result = split_numbers("1 2 3 4 5")
    print(f'result = {result}')
