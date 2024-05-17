from requests import delete

url, user_id = input(), input()
delete(url=f'http://{url}/users/{user_id}')
