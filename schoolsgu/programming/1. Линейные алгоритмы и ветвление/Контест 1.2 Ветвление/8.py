k = int(input())
if k % 10 == 1 and k not in (11, 111):
    print(f'Мне {k} год')
elif k % 10 in (2, 3, 4) and k not in (12, 13, 14, 112, 113, 114):
    print(f'Мне {k} года')
else:
    print(f'Мне {k} лет')
