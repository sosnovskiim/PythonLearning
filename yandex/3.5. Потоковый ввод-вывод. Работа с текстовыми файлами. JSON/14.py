import json

file_name_users, file_name_updates = input(), input()
with open(file_name_users, encoding='utf-8') as file_in:
    users = json.load(file_in)
with open(file_name_updates, encoding='utf-8') as file_in:
    updates = json.load(file_in)
data = dict()
for user in users:
    user_name = user.pop('name')
    data[user_name] = dict()
    for key, value in user.items():
        data[user_name][key] = value
for update in updates:
    user_name = update.pop('name')
    for key, value in update.items():
        if key not in data[user_name] or value > data[user_name][key]:
            data[user_name][key] = value
with open(file_name_users, 'w', encoding='utf-8') as file_out:
    json.dump(data, file_out, ensure_ascii=False, indent=4)

"""
# Пользовательский ввод:
users.json
updates.json

# Содержимое файла users.json
[
    {
        "name": "Ann",
        "address": "Flower st."
    },
    {
        "name": "Bob",
        "address": "Summer st.",
        "phone": "+7 (123) 456-78-90"
    }
]

# Содержимое файла updates.json
[
    {
        "name": "Ann",
        "address": "Awesome st.",
        "phone": "+7 (098) 765-43-21"
    },
    {
        "name": "Bob",
        "address": "Winter st."
    }
]
"""
