from requests import get

url = input()
a = get(f'http://{url}').json()
result = 0
for x in a:
    if isinstance(x, list):
        for y in x:
            try:
                result += int(y)
            except ValueError:
                pass
    else:
        try:
            result += int(x)
        except ValueError:
            pass
print(result)
