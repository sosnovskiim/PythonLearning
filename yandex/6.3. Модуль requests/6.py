from requests import get

url = input()
users = get(f'http://{url}/users').json()
for user in sorted(users, key=lambda d: (d['last_name'], d['first_name'])):
    print(user['last_name'], user['first_name'])
