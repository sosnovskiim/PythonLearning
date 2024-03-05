k = int(input())
d = dict()
with open('text.txt') as f:
    for s in f.read().split():
        if s.isalpha():
            d[s] = d.get(s, 0) + 1
mx = max(d.values())
for i in range(min(k, mx)):
    print(f'{mx - i} - {" ".join(k for k, v in d.items() if v == mx - i)}')
