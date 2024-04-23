with open('input.txt', encoding='utf-8') as file_in:
    n = int(file_in.readline())
    students = list()
    average_grades = list()
    i = 0
    for line in file_in.readlines():
        students.append(f'{line.strip()}\n')
        surname, name, patronymic, year, *grades = line.split()
        grades_sum, grades_cnt = 0, 0
        for grade in grades:
            grades_sum += int(grade)
            grades_cnt += 1
        average_grades.append(grades_sum / grades_cnt)
        j = i
        while j > 0 and average_grades[j] < average_grades[j - 1]:
            average_grades[j], average_grades[j - 1] = average_grades[j - 1], average_grades[j]
            students[j], students[j - 1] = students[j - 1], students[j]
            j -= 1
        i += 1
with open('output.txt', 'w', encoding='utf-8') as file_out:
    file_out.writelines(students)
