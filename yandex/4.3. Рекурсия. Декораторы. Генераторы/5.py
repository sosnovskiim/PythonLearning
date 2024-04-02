def result_accumulator(f):
    cash = dict()

    def dec(*args, method='accumulate'):
        nonlocal cash
        if f not in cash:
            cash[f] = [f(*args)]
        else:
            cash[f].append(f(*args))
        if method == 'drop':
            temp = cash[f]
            cash.clear()
            return temp

    return dec


if __name__ == '__main__':
    @result_accumulator
    def a_plus_b(a, b):
        return a + b


    print(a_plus_b(3, 5, method="accumulate"))
    print(a_plus_b(7, 9))
    print(a_plus_b(-3, 5, method="drop"))
    print(a_plus_b(1, -7))
    print(a_plus_b(10, 35, method="drop"))
