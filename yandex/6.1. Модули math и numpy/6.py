import numpy as np


def multiplication_matrix(n):
    a = np.ones(shape=(n, n), dtype=np.int32)
    a *= np.arange(1, n + 1)
    a = a.T
    a *= np.arange(1, n + 1)
    return a


if __name__ == '__main__':
    print(multiplication_matrix(5))
