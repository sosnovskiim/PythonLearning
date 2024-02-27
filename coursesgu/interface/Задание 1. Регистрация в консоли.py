from string import whitespace
from string import ascii_lowercase
from string import ascii_uppercase
from string import ascii_letters
from string import digits
from string import punctuation


def input_login():
    print('\n Придумайте логин.'
          '\n   Примечание: минимум из 5 символов, может включать только латинские буквы и цифры.')
    result = ''
    while not result:
        temp = input('\n Логин: ')
        if any(c in whitespace for c in set(temp)):
            print('\n Поле не может включать пробельные символы.')
        elif len(temp) > 32:
            print('\n В поле нельзя ввести более 32 символов.')
        elif len(temp) < 5:
            print('\n Логин не может включать меньше 5 символов.')
        elif not all(c in ascii_letters + digits for c in set(temp)):
            print('\n Логин не может включать другие символы, кроме латинских букв и цифр.')
        else:
            result = temp
    return result


def input_password():
    print('\n Придумайте пароль.'
          '\n   Примечание: минимум из 8 символов, может включать только латинские буквы, цифры и спец. символы,'
          '\n   должен включать хотя бы одну строчную букву, хотя бы одну прописную букву,'
          '\n   хотя бы одну цифру и хотя бы один спец. символ.')
    result = ''
    while not result:
        temp = input('\n Пароль: ')
        if any(c in whitespace for c in set(temp)):
            print('\n Поле не может включать пробельные символы.')
        elif len(temp) > 32:
            print('\n В поле нельзя ввести более 32 символов.')
        elif len(temp) < 8:
            print('\n Пароль не может включать меньше 8 символов.')
        elif not all(c in ascii_letters + digits + punctuation for c in set(temp)):
            print('\n Пароль не может включать другие символы, кроме латинских букв, цифр и спец. символов.')
        elif not any(c in ascii_lowercase for c in set(temp)):
            print('\n Пароль должен включать хотя бы одну строчную букву.')
        elif not any(c in ascii_uppercase for c in set(temp)):
            print('\n Пароль должен включать хотя бы одну прописную букву.')
        elif not any(c in digits for c in set(temp)):
            print('\n Пароль должен включать хотя бы цифру.')
        elif not any(c in punctuation for c in set(temp)):
            print('\n Пароль должен включать хотя бы один спец. символ.')
        else:
            temp_ = ''
            while temp != temp_:
                print('\n Повторите только что введённый пароль.')
                temp_ = input('\n Повтор пароля: ')
                if temp != temp_:
                    print('\n Пароли не совпадают.')
                    break
                else:
                    result = temp
    return result


def input_email_address():
    print('\n Введите адрес вашей электронной почты.')
    result = ''
    while not result:
        temp = input('\n Почта: ')
        if any(c in whitespace for c in set(temp)):
            print('\n Поле не может включать пробельные символы.')
        elif len(temp) > 256:
            print('\n В поле нельзя ввести более 256 символов.')
        elif '@' not in set(temp):
            print('\n Адрес электронной почты должен содержать символ @.')
        elif temp[0] == '@' or temp[-1] == '@':
            print('\n Символ @ не может стоять в начале или в конце адреса электронной почты.')
        else:
            result = temp
    return result


def input_phone_number():
    print('\n Введите ваш номер телефона.')
    result = ''
    while not result:
        temp = input('\n Телефон: ')
        if not all(c in digits + '+ ' for c in set(temp)):
            print('\n Номер телефона не может включать другие символы, кроме плюса, цифр и пробелов.')
        elif len(temp) > 32:
            print('\n В поле нельзя ввести более 32 символов.')
        elif temp[:2] != '+7' and temp[0] != '8':
            print('\n Номер телефона должен начинаться с +7 или 8.')
        elif temp[:2] == '+7' and (temp.count('+') != 1 or len(list(filter(lambda d: d.isdigit(), temp[2:]))) != 10):
            print('\n Номер телефона должен содержать ровно 10 цифр после +7 и только один плюс.')
        elif temp[0] == '8' and (temp.count('+') != 0 or len(list(filter(lambda d: d.isdigit(), temp[1:]))) != 10):
            print('\n Номер телефона должен содержать ровно 10 цифр после 8 и ни одного плюса.')
        else:
            result = temp
    return result


def input_last_name():
    result = ''
    while not result:
        temp = input('\n Ваша фамилия: ')
        if not temp:
            break
        elif len(temp) > 256:
            print('\n В поле нельзя ввести более 256 символов.')
        elif not all('A' <= c <= 'z' or 'А' <= c <= 'я' or c in '- ' for c in set(temp)):
            print('\n Фамилия может состоять только из латинских или русских букв,'
                  '\n а также дефисов и пробелов.')
        else:
            result = temp
    return result


def input_fist_name():
    result = ''
    while not result:
        temp = input('\n Ваше имя: ')
        if not temp:
            break
        elif any(c in whitespace for c in set(temp)):
            print('\n Поле не может включать пробельные символы.')
        elif len(temp) > 256:
            print('\n В поле нельзя ввести более 256 символов.')
        elif not all('A' <= c <= 'z' or 'А' <= c <= 'я' for c in set(temp)):
            print('\n Имя может состоять только из латинских или русских букв.')
        else:
            result = temp
    return result


def input_middle_name():
    result = ''
    while not result:
        temp = input('\n Ваше отчество: ')
        if not temp:
            break
        elif any(c in whitespace for c in set(temp)):
            print('\n Поле не может включать пробельные символы.')
        elif len(temp) > 256:
            print('\n В поле нельзя ввести более 256 символов.')
        elif not all('A' <= c <= 'z' or 'А' <= c <= 'я' for c in set(temp)):
            print('\n Отчество может состоять только из латинских или русских букв.')
        else:
            result = temp
    return result


def input_place():
    result = ''
    while not result:
        temp = input('\n Ваше место проживания: ')
        if not temp:
            break
        elif len(temp) > 256:
            print('\n В поле нельзя ввести более 256 символов.')
        elif not all('A' <= c <= 'z' or 'А' <= c <= 'я' or c in '- ' or c in digits for c in set(temp)):
            print('\n Название места проживания может состоять только из латинских и русских букв, '
                  '\n а также дефисов, пробелов и цифр.')
        else:
            result = temp
    return result


def input_about():
    result = ''
    while not result:
        temp = input('\n Расскажите о себе: ')
        if not temp:
            break
        elif len(temp) > 4000:
            print('\n В поле нельзя ввести более 4000 символов.')
        else:
            result = temp
    return result


print('\n Регистрация нового пользователя в системе.')
login = input_login()
password = input_password()
email_address = input_email_address()
phone_number = input_phone_number()
print('\n Примечание: следующие поля являются необязательными и могут остаться пустыми.')
last_name = input_last_name()
first_name = input_fist_name()
middle_name = input_middle_name()
place = input_place()
about = input_about()
unspecified = 'Не указано'
with open('database.txt', 'w') as db:
    db.writelines(f'Логин: {login}'
                  f'\nПароль: {password}'
                  f'\nПочта: {email_address}'
                  f'\nТелефон: {phone_number}'
                  f'\nФамилия: {last_name if last_name else unspecified}'
                  f'\nИмя: {first_name if first_name else unspecified}'
                  f'\nОтчество: {middle_name if middle_name else unspecified}'
                  f'\nМесто проживания: {place if place else unspecified}'
                  f'\nО себе: {about if about else unspecified}')
print('\n Вы успешно зарегестрировались в системе.')
with open('database.txt', 'r') as db:
    [print(f' {s}', end='') for s in db.readlines()]
input()
