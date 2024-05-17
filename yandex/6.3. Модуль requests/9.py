import json
import sys

from requests import put

url, user_id = input(), input()
new_data = dict()
for line in sys.stdin:
    key, value = line.strip().split('=')
    new_data[key] = value
put(url=f'http://{url}/users/{user_id}', data=json.dumps(new_data))
