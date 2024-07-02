import pandas as pd


def get_long(s: pd.Series, min_length=5):
    return s[s >= min_length]


if __name__ == '__main__':
    data = pd.Series([3, 5, 6, 6], ['мир', 'питон', 'привет', 'яндекс'])
    filtered = get_long(data, min_length=6)
    print(data)
    print(filtered)
