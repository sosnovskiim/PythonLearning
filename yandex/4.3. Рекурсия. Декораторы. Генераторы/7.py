def same_type(f):
    def dec(*args):
        t = type(args[0])
        for a in args[1:]:
            if not isinstance(a, t):
                print('Обнаружены различные типы данных')
                return
        return f(*args)

    return dec


if __name__ == '__main__':
    @same_type
    def a_plus_b(a, b):
        return a + b


    print(a_plus_b(3, 5.2) or 'Fail')
    print(a_plus_b(7, '9') or 'Fail')
    print(a_plus_b(-3, 5) or 'Fail')
