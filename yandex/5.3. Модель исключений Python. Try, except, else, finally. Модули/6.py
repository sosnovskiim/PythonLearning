class NoSolutionsError(Exception):
    pass


class InfiniteSolutionsError(Exception):
    pass


def find_roots(a, b, c):
    if not (isinstance(a, (int, float)) or isinstance(b, (int, float)) or isinstance(c, (int, float))):
        raise TypeError
    if a == 0 and c == 0:
        raise InfiniteSolutionsError
    d = b ** 2 - 4 * a * c
    if a == 0 and b == 0 or d < 0:
        raise NoSolutionsError
    else:
        return (-b - d ** 0.5) / (2 * a), (-b + d ** 0.5) / (2 * a)


if __name__ == '__main__':
    print(find_roots(0.0, 0.0, 1.0))
