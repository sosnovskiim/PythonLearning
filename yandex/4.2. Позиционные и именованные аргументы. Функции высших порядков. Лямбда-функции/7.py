def enter_results(*args):
    results.extend(list(args))


def get_sum():
    sm1, sm2 = 0, 0
    for a, b in zip(results[::2], results[1::2]):
        sm1 += a
        sm2 += b
    return round(sm1, 2), round(sm2, 2)


def get_average():
    sm1, sm2 = 0, 0
    for a, b in zip(results[::2], results[1::2]):
        sm1 += a
        sm2 += b
    k = len(results) // 2
    return round(sm1 / k, 2), round(sm2 / k, 2)


results = list()
if __name__ == '__main__':
    enter_results(3.5, 2.14, 45.2, 37.99)
    print(get_sum(), get_average())
    enter_results(5.2, 7.3)
    print(get_sum(), get_average())
    enter_results(1.23, 4.56, 3.14, 2.71, 0, 0)
    print(get_sum(), get_average())
