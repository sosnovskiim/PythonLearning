class CyrillicError(Exception):
    pass


class CapitalError(Exception):
    pass


def name_validation(name):
    if not isinstance(name, str):
        raise TypeError
    cyrillic = {chr(c) for c in range(ord('А'), ord('я') + 1)} | {'Ё', 'ё'}
    if not all(c in cyrillic for c in name):
        raise CyrillicError
    if not name.istitle():
        raise CapitalError
    return name


if __name__ == '__main__':
    print(name_validation("иванов"))
