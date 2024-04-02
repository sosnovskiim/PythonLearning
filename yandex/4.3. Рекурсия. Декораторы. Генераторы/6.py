def merge_sort(a):
    if __name__ == '__main__':
        print(f'# Вызов merge_sort({a})')
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
        if t1[i] < t2[j]:
            a.append(t1[i])
            i += 1
        else:
            a.append(t2[j])
            j += 1
    a.extend(t1[i:])
    a.extend(t2[j:])
    return a


if __name__ == '__main__':
    result = merge_sort([3, 1, 5, 3])
    print(f'result = {result}')
