def make_linear(a):
    if __name__ == '__main__':
        print(f'# Вызов make_linear({a})')
    t = list()
    for x in a:
        if isinstance(x, list):
            t.extend(make_linear(x))
        else:
            t.append(x)
    return t


if __name__ == '__main__':
    result = make_linear([1, [2, [3, 4]], 5, 6])
    print(f'result = {result}')
