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
    return tuple(a)


if __name__ == '__main__':
    result = merge((1, 2), (3, 4, 5))
    print(f'result = {result}')
