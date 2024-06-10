def merge(it1, it2):
    if not hasattr(it1, '__iter__') or not hasattr(it2, '__iter__'):
        raise StopIteration
    it = list()
    i, j = 0, 0
    while i < len(it1) or j < len(it2):
        if i != 0 and i < len(it1):
            if not isinstance(it1[i], it1[i - 1].__class__):
                raise TypeError
            if it1[i] < it1[i - 1]:
                raise ValueError
        if j != 0 and j < len(it2):
            if not isinstance(it2[j], it2[j - 1].__class__):
                raise TypeError
            if it2[j] < it2[j - 1]:
                raise ValueError
        if j == len(it2):
            it.append(it1[i])
            i += 1
        elif i == len(it1):
            it.append(it2[j])
            j += 1
        elif it1[i] < it2[j]:
            it.append(it1[i])
            i += 1
        else:
            it.append(it2[j])
            j += 1
    return it


if __name__ == '__main__':
    print(*merge([3, 2, 1], range(10)))
