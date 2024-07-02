import numpy as np
import pandas as pd


def values(func, start, end, step):
    x = np.arange(start, end + step, step)
    return pd.Series(func(x), index=x)


def min_extremum(data):
    return data.idxmin()


def max_extremum(data):
    return data.idxmax()


if __name__ == '__main__':
    data = values(lambda x: x ** 2 + 2 * x + 1, -1.5, 1.7, 0.1)
    print(data)
    print(min_extremum(data))
    print(max_extremum(data))
