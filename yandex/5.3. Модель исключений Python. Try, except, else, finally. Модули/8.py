from string import ascii_letters, digits


class BadCharacterError(Exception):
    pass


class StartsWithDigitError(Exception):
    pass


def username_validation(username):
    if not isinstance(username, str):
        raise TypeError
    characters = {c for c in ascii_letters} | {c for c in digits} | {'_'}
    if not all(c in characters for c in username):
        raise BadCharacterError
    if username[0] in digits:
        raise StartsWithDigitError
    return username


if __name__ == '__main__':
    print(username_validation("45_user"))
