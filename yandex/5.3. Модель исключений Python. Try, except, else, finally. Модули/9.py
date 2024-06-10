from string import ascii_letters, digits


class CyrillicError(Exception):
    pass


class CapitalError(Exception):
    pass


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


def name_validation(name):
    if not isinstance(name, str):
        raise TypeError
    cyrillic = {chr(c) for c in range(ord('А'), ord('я') + 1)} | {'Ё', 'ё'}
    if not all(c in cyrillic for c in name):
        raise CyrillicError
    if not name.istitle():
        raise CapitalError
    return name


def user_validation(last_name=None, first_name=None, username=None, **kwargs):
    if kwargs or last_name is None or first_name is None or username is None:
        raise KeyError
    if not (isinstance(last_name, str) or isinstance(first_name, str) or isinstance(username, str)):
        raise TypeError
    name_validation(last_name)
    name_validation(first_name)
    username_validation(username)
    return {'last_name': last_name, 'first_name': first_name, 'username': username}


if __name__ == '__main__':
    print(user_validation(last_name="Иванов", first_name="Иван", username="ivanych45"))
