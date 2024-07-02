import numpy as np


def snake(m, n, direction='H'):
    a = np.arange(1, m * n + 1, dtype=np.int16)
    if direction == 'V':
        a = a.reshape(m, n).T
        a[:, 1::2] = a[::-1, 1::2]
    else:
        a = a.reshape(n, m)
        a[1::2] = a[1::2, ::-1]
    return a


if __name__ == '__main__':
    print(snake(5, 3, direction='V'))
