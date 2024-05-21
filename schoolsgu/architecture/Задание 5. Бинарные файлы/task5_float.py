import struct

result: bytes = bytes()
while not result:
    s = input('Введите вещественное число от 2.2250738585072014e-308 до 1.7976931348623157e+308: ')
    try:
        result: bytes = struct.pack('f', float(s))
        print(f'Созданный бинарное файл из числа {s}: {str(result)[2:-1]}')
    except ValueError:
        print(f'Строка {s} не является вещественным числом.')
    except OverflowError:
        print(f'Число {s} не соответствует двухбайтовому формату float.')
number: float = struct.unpack('f', result)[0]
print(f'Беззнаковое число, полученное из бинарного файла: {number}')
