def answer(f):
    def dec(*args, **kwargs):
        return f'Результат функции: {f(*args, **kwargs)}'

    return dec


if __name__ == '__main__':
    @answer
    def a_plus_b(a, b):
        return a + b


    print(a_plus_b(3, 5))
    print(a_plus_b(7, 9))
