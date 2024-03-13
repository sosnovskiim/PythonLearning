"""
 1. Определите, сколько учеников в Центральном округе (Ц) выбрали в качестве любимого предмета английский язык.

 2. Рассчитайте средний тестовый балл у учеников Восточного округа (В).

 3. Найдите процентное соотношение числа участников из округов с кодами «З», «ЮЗ» и «Ц».

 4. Создайте файл res.csv, в который вынесите информацию об учениках, выбравших математику.
    Названия столбцов должны быть как в исходной таблице.
"""
import csv

DISTRICT, STUDENT, SUBJECT, SCORE = 'округ', 'код ученика', 'любимый предмет', 'балл'
cnt1 = 0
sm2, cnt2 = 0, 0
cnt31, cnt32, cnt33 = 0, 0, 0
students_loves_math = list()
with open('var3.csv', encoding='utf-8') as f:
    reader = csv.DictReader(f, delimiter=';')
    for row in reader:
        # 1
        if row[DISTRICT] == 'Ц' and row[SUBJECT] == 'английский язык':
            cnt1 += 1
        # 2
        if row[DISTRICT] == 'В':
            sm2 += int(row[SCORE])
            cnt2 += 1
        # 3
        if row[DISTRICT] == 'З':
            cnt31 += 1
        if row[DISTRICT] == 'ЮЗ':
            cnt32 += 1
        if row[DISTRICT] == 'Ц':
            cnt33 += 1
        # 4
        if row[SUBJECT] == 'математика':
            students_loves_math.append(row)
# 1
print(f'\n1. Выбрали английский язык в Центральном округе:'
      f'\n   {cnt1}')
# 2
print(f'\n2. Средний балл по Восточному округу:'
      f'\n   {sm2 / cnt2:.2f}')
# 3
sm3 = cnt31 + cnt32 + cnt33
print(f'\n3. Участников из:'
      f'\n   Западного округа - {cnt31 / sm3 * 100:.2f}%'
      f'\n   Юго-западного округа - {cnt32 / sm3 * 100:.2f}%'
      f'\n   Центрального округа - {cnt33 / sm3 * 100:.2f}%')
# 4
print('\n4. В файл res.csv вынесена информация об учениках, выбравших математику.')
with open('res.csv', 'w', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=list(students_loves_math[0].keys()), delimiter=';', lineterminator='\r')
    writer.writeheader()
    for row in students_loves_math:
        writer.writerow(row)
