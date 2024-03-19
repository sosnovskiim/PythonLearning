def make_matrix(size, value=0):
    if isinstance(size, tuple):
        a = [[value for _ in range(size[0])] for _ in range(size[1])]
    else:
        a = [[value for _ in range(size)] for _ in range(size)]
    return a


if __name__ == '__main__':
    result = make_matrix(3)
    print(f'result = {result}')
