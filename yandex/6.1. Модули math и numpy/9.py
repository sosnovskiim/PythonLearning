import numpy as np


def rotate(a, d):
    return np.rot90(a, -d // 90)


if __name__ == '__main__':
    print(rotate(np.arange(12).reshape(3, 4), 270))
