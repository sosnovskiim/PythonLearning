import struct

result: bytes = bytes()
while not result:
    s = input('Введите вещественное число от -65504.0 до 65504.0: ')
    if '.' not in str(s):
        print(f'Строка {s} не является вещественным числом.')
    else:
        try:
            result: bytes = struct.pack('e', float(s))
            print(f'Созданный бинарное файл из числа {s}: {str(result)[2:-1]}')
        except OverflowError:
            print(f'Число {s} не соответствует двухбайтовому формату float.')
number: float = struct.unpack('e', result)[0]
print(f'Беззнаковое число, полученное из бинарного файла: {number}')
