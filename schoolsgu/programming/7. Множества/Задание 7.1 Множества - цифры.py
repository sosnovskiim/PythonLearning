# На одной строке записаны целые числа, разделённые пробельными символами.
# Найти все такие цифры, которые не встречаются в записи этих чисел.
from string import digits

s = set(digits)
for x in input().split():
    s -= set(x)
print(' '.join(sorted(s)))
