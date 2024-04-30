from itertools import product


def grasshopper(start, finish, length):
    result = list()
    for path in product(range(start - length, finish + length + 1), repeat=length + 1):
        if path[0] > start:
            break
        cnt = path.count(finish)
        if path[0] == start and path[-1] == finish and (start != finish and cnt == 1 or start == finish and cnt == 2):
            for i, j in zip(path, path[1:]):
                if i == j or abs(i - j) > 2:
                    break
            else:
                result.append(list(path))
    return result


if __name__ == '__main__':
    result = grasshopper(1, 10, 5)
    print(*result, sep="\n")
