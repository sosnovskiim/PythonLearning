with open('input.txt', encoding='utf-8') as file_in:
    n = int(file_in.readline())
    students = list()
    SURNAME, NAME, PATRONYMIC, YEAR, GRADES = 'surname', 'name', 'patronymic', 'year', 'grades'
    i = 0
    for line in file_in.readlines():
        surname, name, patronymic, year, *grades = line.split()
        students.append({SURNAME: surname, NAME: name, PATRONYMIC: patronymic, YEAR: year, GRADES: ' '.join(grades)})
        j = i
        while j > 0 and (surname < students[j - 1][SURNAME] or year > students[j - 1][YEAR]):
            students[j], students[j - 1] = students[j - 1], students[j]
            j -= 1
        i += 1
with open('output.txt', 'w', encoding='utf-8') as file_out:
    for student in students:
        file_out.write(f'{" ".join(student.values())}\n')
