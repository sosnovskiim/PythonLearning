def make_list(length, value=0):
    a = [value for _ in range(length)]
    return a


if __name__ == '__main__':
    result = make_list(3)
    print(f'result = {result}')
