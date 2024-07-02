import numpy as np


def make_board(n):
    a = np.ones(shape=(n, n), dtype=np.int8)
    a[::2, 1::2] = 0
    a[1::2, ::2] = 0
    return a


if __name__ == '__main__':
    print(make_board(6))
