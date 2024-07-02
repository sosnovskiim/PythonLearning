import numpy as np


def stairs(a):
    r = np.array([a])
    for i in range(1, a.shape[0]):
        r = np.append(r, np.array([np.roll(a, i)]), axis=0)
    return r


if __name__ == '__main__':
    print(stairs(np.arange(5)))
