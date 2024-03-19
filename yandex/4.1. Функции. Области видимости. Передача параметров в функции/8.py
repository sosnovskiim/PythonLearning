def is_palindrome(value):
    if isinstance(value, int):
        return str(value) == str(value)[::-1]
    return value == value[::-1]


if __name__ == '__main__':
    result = is_palindrome(123)
    print(f'result = {result}')
