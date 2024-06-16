"""
Отсортировать числа по убыванию суммы цифр, кроме разряда единиц.
"""
from random import randint
from time import perf_counter_ns

numbers = list()
for _ in range(10):
    x = randint(0, 999)
    t, sm = x // 10, 0
    while t > 0:
        sm += t % 10
        t //= 10
    numbers.append((sm, x))
print(f'initial array is [{", ".join(map(str, (n[1] for n in numbers)))}]')


def print_result(sorting_method):
    tmp = perf_counter_ns()
    a = numbers.copy()
    if sorting_method.__name__ == quick_sort.__name__:
        fst, lst = 0, len(numbers) - 1
        sorted_numbers = sorting_method(a, fst, lst)
    else:
        sorted_numbers = sorting_method(a)
    print(f'{sorting_method.__name__} completed in {(perf_counter_ns() - tmp) / 1000:.1f} ms\n'
          f'{sorting_method.__name__} result is [{", ".join(map(str, (n[1] for n in sorted_numbers)))}]')


def quick_sort(a, fst, lst):
    if fst >= lst:
        return
    p = a[randint(fst, lst)]
    i, j = fst, lst
    while i <= j:
        while a[i] > p:
            i += 1
        while a[j] < p:
            j -= 1
        if i <= j:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1
    quick_sort(a, fst, j)
    quick_sort(a, i, lst)
    return a


def heap_sort(a):
    for i in range(len(a) // 2 - 1, -1, -1):
        push_down(a, len(a), i)
    for i in range(len(a) - 1, 0, -1):
        a[i], a[0] = a[0], a[i]
        push_down(a, i, 0)
    return a


def push_down(a, lst, fst):
    m = fst
    lt, rt = 2 * fst + 1, 2 * fst + 2
    if lt < lst and a[fst] > a[lt]:
        m = lt
    if rt < lst and a[m] > a[rt]:
        m = rt
    if m != fst:
        a[fst], a[m] = a[m], a[fst]
        push_down(a, lst, m)


def merge_sort(a):
    if len(a) > 1:
        mid = len(a) // 2
        t1 = merge_sort(a[:mid])
        t2 = merge_sort(a[mid:])
        a = merge(t1, t2)
    return a


def merge(t1, t2):
    a = list()
    i, j = 0, 0
    while i < len(t1) and j < len(t2):
        if t1[i] > t2[j]:
            a.append(t1[i])
            i += 1
        else:
            a.append(t2[j])
            j += 1
    a.extend(t1[i:])
    a.extend(t2[j:])
    return a


def tim_sort(a):
    return sorted(a, reverse=True)


print_result(sorting_method=quick_sort)
print_result(sorting_method=heap_sort)
print_result(sorting_method=merge_sort)
print_result(sorting_method=tim_sort)
