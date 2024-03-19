def month(number, language='ru'):
    ru = {1: 'Январь', 2: 'Февраль', 3: 'Март', 4: 'Апрель',
          5: 'Май', 6: 'Июнь', 7: 'Июль', 8: 'Август',
          9: 'Сентябрь', 10: 'Октябрь', 11: 'Ноябрь', 12: 'Декабрь'}
    en = {1: 'January', 2: 'February', 3: 'March', 4: 'April',
          5: 'May', 6: 'June', 7: 'July', 8: 'August',
          9: 'September', 10: 'October', 11: 'November', 12: 'December'}
    return ru[number] if language == 'ru' else en[number]


if __name__ == '__main__':
    result = month(1, "en")
    print(f"result = '{result}'")
