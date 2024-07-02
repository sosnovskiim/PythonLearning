import pandas as pd


def length_stats(t: str):
    t = ''.join(c.lower() for c in t if c.isalpha() or c == ' ')
    d = {w: len(w) for w in t.split()}
    s = pd.Series({i: d[i] for i in sorted(d.keys())})
    return s[s % 2 != 0], s[s % 2 == 0]


if __name__ == '__main__':
    odd, even = length_stats('Лес, опушка, странный домик. Лес, опушка и зверушка.')
    print(odd)
    print(even)
