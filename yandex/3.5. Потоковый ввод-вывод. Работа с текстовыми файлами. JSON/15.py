import json

with open('scoring.json', encoding='utf-8') as file_in:
    scoring = json.load(file_in)
score = 0
for group in scoring:
    cnt = 0
    for test in group['tests']:
        answer = input()
        if answer == test['pattern']:
            cnt += 1
    score += group['points'] // len(group['tests']) * cnt
print(score)

"""
# Пользовательский ввод:
4
12
3
100
0

# Содержимое файла scoring.json
[
    {
        "points": 10,
        "tests": [
            {
                "input": "2 2",
                "pattern": "4"
            },
            {
                "input": "4 3",
                "pattern": "7"
            }
        ]
    },
    {
        "points": 30,
        "tests": [
            {
                "input": "2 1",
                "pattern": "3"
            },
            {
                "input": "25 4",
                "pattern": "29"
            },
            {
                "input": "3 -3",
                "pattern": "0"
            }
        ]
    }
]
"""
