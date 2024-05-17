import json

from requests import post

url, username, last_name, first_name, email = input(), input(), input(), input(), input()
user = {'username': username, 'last_name': last_name, 'first_name': first_name, 'email': email}
post(url=f'http://{url}/users', data=json.dumps(user))
