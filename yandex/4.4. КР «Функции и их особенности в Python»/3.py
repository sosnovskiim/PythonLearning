def find_pair(*numbers, div=6):
    ri, rj = 0, 1
    smr = None
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            smt = numbers[i] + numbers[j]
            if i != j and smt % div == 0 and (smr is None or smt > smr or smt == smr and j > rj):
                ri, rj = i, j
                smr = smt
    return numbers[ri], numbers[rj]


if __name__ == '__main__':
    numbers = [41, 56, 54, 6, 31, 81, 77, 83, 86, 15]
    result = find_pair(*numbers, div=3)
    print(*result)
