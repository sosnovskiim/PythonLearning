import os

os.chdir(os.path.join(os.curdir, 'Задание 2. Папка с файлами'))

for file in os.listdir():
    print(file)
