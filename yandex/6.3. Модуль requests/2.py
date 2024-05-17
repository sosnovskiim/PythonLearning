from requests import get

url = input()
result = 0
while x := int(get(f'http://{url}').content.decode()):
    result += x
print(result)
