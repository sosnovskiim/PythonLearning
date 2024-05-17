import sys

from requests import get

url = input()
paths = [line.strip() for line in sys.stdin]
result = 0
for path in paths:
    result += sum(get(f'http://{url}{path}').json())
print(result)
