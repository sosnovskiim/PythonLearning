def to_string(*args, sep=' ', end='\n'):
    return sep.join(map(str, args)) + end


if __name__ == '__main__':
    data = [7, 3, 1, "hello", (1, 2, 3)]
    result = to_string(*data, sep=", ", end="!")
    print(f"result = '{result}'")
