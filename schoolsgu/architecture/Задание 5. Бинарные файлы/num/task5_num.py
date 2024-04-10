import struct

result = ''
while not result:
    s = input('Введите целое число от -32768 до 32767: ')
    try:
        result = struct.pack('h', int(s))
        print(f'Бинарное представление числа {s}: {result}')
    except ValueError:
        print(f'Строка {s} не является целым числом.')
    except struct.error:
        print(f'Число {s} не соответствует формату short.')

