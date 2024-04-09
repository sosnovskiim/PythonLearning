import os
import fnmatch
import re
from keyword import kwlist

os.chdir(os.path.join(os.curdir, 'folder'))
for file in fnmatch.filter(os.listdir(), f'{input("Введите первую букву имени файла: ")}????*[0-9]?.txt'):
    with open(file, encoding='utf-8') as f:
        print(f'\nFound in file {file}')
        for line in f.readlines():
            for t in re.findall(r'((?:[01]\d|2[0-3]):[0-5]\d(?::[0-5]\d)?)', line):
                if t:
                    print(f'TIME - {t}')
            for t in re.findall(r'([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)', line):
                if t:
                    print(f'MAIL - {t}')
            for t in re.findall(r'(https?://[^\"\s>]+)', line):
                if t:
                    print(f'URL - {t}')
            for t in re.findall(r'([a-zA-Z_][a-zA-Z0-9_]*)', line):
                if t and t != 'l' and t not in kwlist:
                    print(f'VAR - {t}')
