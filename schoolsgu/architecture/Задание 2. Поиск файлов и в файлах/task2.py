import os

os.chdir(os.path.join(os.curdir, 'folder'))
for file in os.listdir():
    period = file.rfind('.')
    if file[0] == 'p' and file[:period][-2].isdigit() and len(file[:period]) >= 7 and file[period + 1:] == 'txt':
        print(file)
