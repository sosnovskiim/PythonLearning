import os
import shutil

print(f'\n1. Текущая директория:\n{os.getcwd()}')
input()

print(f'2 Текущий пользователь:\n{os.getlogin()}')
input()

d = {'posix': 'MacOS', 'nt': 'Windows', 'java': 'Linux'}
print(f'3. Тип операционной системы:\n{d[os.name]}')
input()

print('4. Проверка существования файла:'
      f"\n{'Файл Задание 2. Папка с файлами.txt существует' if os.path.isfile('Задание 2. Папка с файлами.txt') else 'Файл Задание 2. Папка с файлами.txt не существует'}")
input()

print('5. Содержимое текущей папки:')
[print(d_) for d_ in os.listdir()]
input()

print('6. Текущая директория с учетом вложенности:')
for root, dirs, files in os.walk(os.getcwd()):
    print(f'{root}')
    [print(f'\t{d}') for d in dirs]
    [print(f'\t{f}') for f in files]
input()

dir_name = 'Задание 2. Папка с файлами'
print('7. Создание папки:')
if os.path.isdir(dir_name):
    print(f'Папка {dir_name} уже существует')
else:
    os.mkdir(os.path.join(os.curdir, dir_name))
    print(f'Папка {dir_name} создана')
input()

print('8. Переход в заданную папку:')
os.chdir(os.path.join(os.curdir, dir_name))
print(os.getcwd())
input()

file_name = ''
while not file_name:
    file_name = input('9. Назовите файл, создаваемый в текущей директории:\n')
    if file_name:
        with open(file_name, 'w') as f:
            f.write(os.getlogin())
        print(f'Файл {file_name} успешно создан')
    elif os.path.isfile(file_name):
        print(f'Файл {file_name} уже создан')

print('\n10. Проверка создания файла:')
if os.path.isfile(file_name):
    print(f'Создан файл {file_name} с записью {os.getlogin()}')
else:
    print('Файл не создан')
input()

print(f'11. Абсолютный путь до файла {file_name}: {os.path.join(os.getcwd(), file_name)}\n'
      f'    Его размер: {os.path.getsize(file_name)} байт')
input()

shutil.copy(os.path.join(os.curdir, file_name), '../')
if os.path.isfile(os.path.join('../', file_name)):
    print('12. Файл успешно скопирован')
else:
    print('12. Файл не скопирован')
input()

os.chdir('../')
print('13. Переход на уровень выше и текущая директория с учетом вложенности:')
for root, dirs, files in os.walk(os.getcwd()):
    print(f'{root}')
    [print(f'\t{d}') for d in dirs]
    [print(f'\t{f}') for f in files]
input()

print('14. Содержимое ранее скопированного файла:')
with open(file_name) as f:
    print(f.read())
input()

shutil.rmtree(os.path.join(os.curdir, dir_name))
if os.path.isdir(dir_name):
    print(f'15. Папка {dir_name} не удалена')
else:
    print(f'15. Папка {dir_name} успешно удалена')
input()

if os.path.isfile(file_name):
    os.remove(file_name)
    print(f'16. Файл {file_name} удален')
else:
    print(f'16. Файл {file_name} не существует')
input()

if os.path.isdir(dir_name) or os.path.isfile(file_name):
    print('17. Что-то не так')
else:
    print('17. Все в порядке')
for root, dirs, files in os.walk(os.getcwd()):
    print(f'{root}')
    [print(f'\t{d}') for d in dirs]
    [print(f'\t{f}') for f in files]
input()
