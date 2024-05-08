import struct

result: bytes = bytes()
while not result:
    s = input('Введите целое число от -32768 до 32767: ')
    try:
        result: bytes = struct.pack('h', int(s))
        print(f'Созданный бинарное файл из числа {s}: {str(result)[2:-1]}')
    except ValueError:
        print(f'Строка {s} не является целым числом.')
    except struct.error:
        print(f'Число {s} не соответствует двухбайтовому формату short.')
number: int = struct.unpack('H', result)[0]
print(f'Беззнаковое число, полученное из бинарного файла: {number}')
