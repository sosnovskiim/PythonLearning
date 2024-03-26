def make_equation(*numbers):
    if __name__ == '__main__':
        print(f'# Вызов make_equation({", ".join(map(str, numbers))})')
    if len(numbers) == 1:
        return numbers[0]
    return f'({make_equation(*numbers[:len(numbers) - 1])}) * x + {numbers[-1]}'


if __name__ == '__main__':
    result = make_equation(3, 2, 1)
    print(f"result = '{result}'")
