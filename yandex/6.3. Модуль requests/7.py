import sys

from requests import get

url, user_id = input(), int(input())
text = ''
for line in sys.stdin:
    text += line
response = get(f'http://{url}/users/{user_id}')
if response.status_code == 200:
    user = response.json()
    print(text.format(id=user['id'], username=user['username'],
                      last_name=user['last_name'], first_name=user['first_name'], email=user['email']))
else:
    print('Пользователь не найден')
