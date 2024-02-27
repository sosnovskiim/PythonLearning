# В каждой строке входного файла "input.txt" записано от 0 до 100 чисел.
# Найти числа, которые встречаются только в первой половине строк.
with open('input.txt', 'r') as f:
    a = [[x for x in s.split()] for s in f.readlines()]
s1, s2 = set(), set()
for i in range(len(a) // 2):
    for j in range(len(a[i])):
        s1.add(a[i][j])
for i in range(len(a) // 2, len(a)):
    for j in range(len(a[i])):
        s2.add(a[i][j])
with open('output.txt', 'w') as f:
    f.write(' '.join(sorted(s1 - s2)))
