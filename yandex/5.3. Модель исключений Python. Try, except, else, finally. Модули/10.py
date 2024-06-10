from string import ascii_letters, digits
from hashlib import sha256


class MinLengthError(Exception):
    pass


class PossibleCharError(Exception):
    pass


class NeedCharError(Exception):
    pass


def password_validation(password, min_length=8, possible_chars=ascii_letters + digits, at_least_one: () = str.isdigit):
    if not isinstance(password, str):
        raise TypeError
    if len(password) < min_length:
        raise MinLengthError
    if not all(c in possible_chars for c in password):
        raise PossibleCharError
    if not any(at_least_one(c) for c in password):
        raise NeedCharError
    return sha256(password.encode()).hexdigest()


if __name__ == '__main__':
    print(password_validation("Hello12345"))
