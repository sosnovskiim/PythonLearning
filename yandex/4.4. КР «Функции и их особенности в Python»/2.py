def add_number(number):
    numbers.append(number)


def get_sum():
    return f'{" + ".join(map(str, numbers))} = {sum(numbers)}'


numbers = list()
if __name__ == '__main__':
    add_number(7)
    add_number(2)
    print(get_sum())
    add_number(5)
    print(get_sum())
