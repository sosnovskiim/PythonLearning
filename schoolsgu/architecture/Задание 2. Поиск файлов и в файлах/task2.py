import os
import fnmatch
import re
from keyword import kwlist

os.chdir(os.path.join(os.curdir, 'folder'))
for file in fnmatch.filter(os.listdir(), 'p????*[0-9]?.txt'):
    with open(file, encoding='utf-8') as f:
        print(f'\nFound in file {file}')
        for line in f.readlines():
            time_temp = re.findall(r'((?:[01]\d|2[0-3])\:(?:[0-5]\d)(?:\:[0-5]\d)?)', line)
            for t in time_temp:
                if t:
                    print(t)
            mail_temp = re.findall(r'([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)', line)
            for t in mail_temp:
                if t:
                    print(t)
            url_temp = re.findall(r'(https?://[^\"\s>]+)', line)
            for t in url_temp:
                if t:
                    print(t)
            var_temp = re.findall(r'([a-zA-Z_][a-zA-Z0-9_]*)', line)
            for t in var_temp:
                if t and t not in kwlist:
                    print(t)
