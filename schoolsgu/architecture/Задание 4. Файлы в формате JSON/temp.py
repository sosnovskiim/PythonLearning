import json

with open('data.json') as in_file:
    data = json.load(in_file)
print(data)
data['marks'].extend([5, 5])
s = json.dumps(data)
print(s)
with open('res.json', 'w') as out_file:
    json.dump(data, out_file, indent=2, sort_keys=True)
