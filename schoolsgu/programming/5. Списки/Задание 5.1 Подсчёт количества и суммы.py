'''
Прочитать целые числа, записанные на одной строке и разделённые запятыми.
Подсчитать количество элементов с номерами от start до stop, которые не делятся на свою старшую цифру.
А также сумму составных чисел среди элементов этого набора, принадлежащих заданному отрезку [A, B].
'''
from math import sqrt

data = list(map(int, input().split(',')))
start, stop = int(input('start: ')), int(input('stop: '))
a, b = int(input('A: ')), int(input('B: '))
cnt1, cnt2 = 0, 0
for i in range(len(data)):
    if start <= i <= stop:
        d, t = 0, data[i]
        while t > 0:
            d = t % 10
            t //= 10
        if data[i] % d != 0:
            cnt1 += 1
    if a <= data[i] <= b:
        for d in range(int(sqrt(data[i]))):
            if data[i] % d == 0:
                cnt2 += 1
                break
print(cnt1, cnt2)
