from requests import get

url, key = input(), input()
d = get(f'http://{url}').json()
try:
    print(d[key])
except KeyError:
    print('No data')
