import pandas as pd


def length_stats(t: str):
    t = ''.join(c.lower() for c in t if c.isalpha() or c == ' ')
    d = {w: len(w) for w in t.split()}
    return pd.Series({i: d[i] for i in sorted(d.keys())})


if __name__ == '__main__':
    print(length_stats('Лес, опушка, странный домик. Лес, опушка и зверушка.'))
