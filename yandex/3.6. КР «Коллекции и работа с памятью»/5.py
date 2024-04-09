import json
from collections import defaultdict
from sys import stdin

temp = defaultdict(set)
for j in [int(i) for i in stdin]:
    for n in range(2, j + 1):
        d = 2
        while d * d <= n and n % d != 0:
            d += 1
        if d * d > n and j % n == 0:
            temp[str(n)].add(j)
result = dict()
for k, v in temp.items():
    result[k] = sorted(v)
with open('result.json', 'w') as file_out:
    json.dump(result, file_out, indent=4)
