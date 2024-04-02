def cycle(a):
    while a:
        for x in a:
            yield x


if __name__ == '__main__':
    print(*(x for _, x in zip(range(15), cycle([1, 2, 3, 4]))))
