import json
from sys import stdin

file_name = input()
with open(file_name, encoding='utf-8') as file_in:
    data = json.load(file_in)
for line in stdin:
    key, _, value = line.split()
    data[key] = value
with open(file_name, 'w', encoding='utf-8') as file_out:
    json.dump(data, file_out, ensure_ascii=False, indent=4)

"""
# Пользовательский ввод:
data.json
one == один
two == два
three == три

# Содержимое файла data.json
{
    "one": 1,
    "three": 2
}
"""
