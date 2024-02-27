'''
Прочитать N целых чисел.
Удалить из этого списка (не создавая новый)
максимальные элементы.
'''
n = int(input())
data = []
mx = None
for x in input().split():
    data.append(x)
    if mx is None or mx < x:
        mx = x
i = 0
while i < len(data):
    if data[i] == mx:
        del data[i]
    else:
        i += 1
print(' '.join(data))
