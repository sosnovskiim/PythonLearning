"""
Отсортировать вакансии по должности,
при равенстве по убыванию опыта работы,
при равенстве по возрастанию зарплаты.
"""
from csv import DictReader, DictWriter
from time import perf_counter_ns

with open('vacancies.csv') as file_in:
    reader = DictReader(file_in, delimiter=';')
    vacancies: list = [row for row in reader]


def write_csv(file_name, sorting_method):
    with open(file_name, 'w') as file_out:
        writer = DictWriter(f=file_out, fieldnames=list(vacancies[0].keys()), delimiter=';', lineterminator='\r')
        writer.writeheader()
        tmp = perf_counter_ns()
        sorted_vacancies = sorting_method()
        print(f'{sorting_method.__name__} completed in {(perf_counter_ns() - tmp) / 1000:.1f} ms')
        for row in sorted_vacancies:
            writer.writerow(row)


def bubble_sort():
    a = [row.copy() for row in vacancies]
    for i in range(len(a)):
        for j in range(len(a) - 1 - i):
            if a[j][t] > a[j + 1][t] or \
                    a[j][t] == a[j + 1][t] and int(a[j][e]) < int(a[j + 1][e]) or \
                    a[j][t] == a[j + 1][t] and int(a[j][e]) == int(a[j + 1][e]) and int(a[j][s]) > int(a[j + 1][s]):
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


def selection_sort():
    a = [row.copy() for row in vacancies]
    for i in range(len(a)):
        m = i
        for j in range(i + 1, len(a)):
            if a[j][t] < a[m][t] or \
                    a[j][t] == a[m][t] and int(a[j][e]) > int(a[m][e]) or \
                    a[j][t] == a[m][t] and int(a[j][e]) == int(a[m][e]) and int(a[j][s]) < int(a[m][s]):
                m = j
        if i != m:
            a[i], a[m] = a[m], a[i]
    return a


def stable_selection_sort():
    a = [row.copy() for row in vacancies]
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i][t] > a[j][t] or \
                    a[i][t] == a[j][t] and int(a[i][e]) < int(a[j][e]) or \
                    a[i][t] == a[j][t] and int(a[i][e]) == int(a[j][e]) and int(a[i][s]) > int(a[j][s]):
                a[i], a[j] = a[j], a[i]
    return a


def insertion_sort():
    a = [row.copy() for row in vacancies]
    for i in range(1, len(a)):
        j = i
        while j > 0 and a[j][t] < a[j - 1][t] or \
                a[j][t] == a[j - 1][t] and int(a[j][e]) > int(a[j - 1][e]) or \
                a[j][t] == a[j - 1][t] and int(a[j][e]) == int(a[j - 1][e]) and int(a[j][s]) < int(a[j - 1][s]):
            a[j], a[j - 1] = a[j - 1], a[j]
            j -= 1
    return a


c, t, s, e = 'company', 'title', 'salary', 'experience'
write_csv(file_name='vacancies_bubble_sort.csv', sorting_method=bubble_sort)
write_csv(file_name='vacancies_selection_sort.csv', sorting_method=selection_sort)
write_csv(file_name='vacancies_stable_selection_sort.csv', sorting_method=stable_selection_sort)
write_csv(file_name='vacancies_insertion_sort.csv', sorting_method=insertion_sort)
