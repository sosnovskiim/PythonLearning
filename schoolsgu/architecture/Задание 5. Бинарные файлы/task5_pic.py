import array
from itertools import chain

title = """
Что сделать с рисунком?
1. Преобразовать в негатив
2. Осветлить
3. Затемнить
4. Отразить слева направо
5. Отразить сверху вниз
6. Преобразовать в оттенки серого
7. Поворот против часовой стрелки
8. Поворот по часовой стрелке
0. Вернуть изначальное изображение
Введите номер операции, чтобы совершить ее: """
width, height = 400, 400
with open('in.bmp', 'rb') as file_in:
    head = file_in.read(54)
    b = [[[i for i in file_in.read(3)] for _ in range(width)] for _ in range(height)]
while o := input(title):
    result = 'Выход из программы.'
    if o == '1':
        for i in range(height):
            for j in range(width):
                for k in range(3):
                    b[i][j][k] = 255 - b[i][j][k]
        result = 'Рисунок преобразован в негатив.'
    elif o == '2':
        c = 100
        for i in range(height):
            for j in range(width):
                for k in range(3):
                    if b[i][j][k] + c < 0:
                        b[i][j][k] = 0
                    elif b[i][j][k] + c > 255:
                        b[i][j][k] = 255
        result = 'Рисунок осветлен.'
    elif o == '3':
        c = -200
        for i in range(height):
            for j in range(width):
                for k in range(3):
                    if b[i][j][k] + c < 0:
                        b[i][j][k] = 0
                    elif b[i][j][k] + c > 255:
                        b[i][j][k] = 255
        result = 'Рисунок затемнен.'
    elif o == '4':
        for i in range(height):
            for j in range(width // 2):
                for k in range(3):
                    b[i][j][k], b[i][width - j - 1][k] = b[i][width - j - 1][k], b[i][j][k]
        result = 'Рисунок отражен слева направо.'
    elif o == '5':
        for i in range(height // 2):
            for j in range(width):
                for k in range(3):
                    b[i][j][k], b[height - i - 1][j][k] = b[height - i - 1][j][k], b[i][j][k]
        result = 'Рисунок отражен сверху вниз.'
    elif o == '6':
        for i in range(height):
            for j in range(width):
                c = 0
                for k in range(3):
                    c += b[i][j][k]
                c //= 3
                for k in range(3):
                    b[i][j][k] = c
        result = 'Рисунок преобразован в оттенки серого.'
    elif o == '7':
        c = [[[k for k in b[i][j]] for j in range(width)] for i in range(height)]
        for i in range(height // 2):
            for j in range(width // 2):
                for k in range(3):
                    b[j][height - i - 1][k] = c[i][j][k]
        for i in range(height // 2):
            for j in range(width // 2, width):
                for k in range(3):
                    b[j][height - i - 1][k] = c[i][j][k]
        for i in range(height // 2, height):
            for j in range(width // 2, width):
                for k in range(3):
                    b[j][height - i - 1][k] = c[i][j][k]
        for i in range(height // 2, height):
            for j in range(width // 2):
                for k in range(3):
                    b[j][height - i - 1][k] = c[i][j][k]
        result = 'Рисунок повернут против часовой стрелки'
    elif o == '8':
        c = [[[k for k in b[i][j]] for j in range(width)] for i in range(height)]
        for i in range(height // 2):
            for j in range(width // 2):
                for k in range(3):
                    b[width - j - 1][i][k] = c[i][j][k]
        for i in range(height // 2):
            for j in range(width // 2, width):
                for k in range(3):
                    b[width - j - 1][i][k] = c[i][j][k]
        for i in range(height // 2, height):
            for j in range(width // 2, width):
                for k in range(3):
                    b[width - j - 1][i][k] = c[i][j][k]
        for i in range(height // 2, height):
            for j in range(width // 2):
                for k in range(3):
                    b[width - j - 1][i][k] = c[i][j][k]
        result = 'Рисунок повернут по часовой стрелке'
    elif o == '0':
        with open('in.bmp', 'rb') as file_in:
            head = file_in.read(54)
            b = [[[i for i in file_in.read(3)] for _ in range(width)] for _ in range(height)]
    a = array.array('B', [i for i in chain.from_iterable([j for j in chain.from_iterable(b)])])
    with open('out.bmp', 'wb') as file_out:
        file_out.write(head)
        file_out.write(a.tobytes())
    print(result)
