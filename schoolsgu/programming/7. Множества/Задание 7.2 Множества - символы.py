# Дано N строк, состоящих из латинских букв в верхнем и нижнем регистре,
# цифр и различных символов, в том числе пробельных.
# Найти буквы, не встречающиеся ни в одной из строк.
from string import ascii_lowercase

n = int(input())
s = set(ascii_lowercase)
for _ in range(n):
    s -= set(input().lower())
print(' '.join(sorted(s)))
