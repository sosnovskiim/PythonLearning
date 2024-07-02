import pandas as pd


def cheque(s: pd.Series, **k):
    df = pd.DataFrame({'product': [i for i in s.sort_index().index if i in k]})
    df['price'] = pd.Series(s[df['product']].values)
    df['number'] = pd.Series(pd.Series(k)[df['product']].values)
    df['cost'] = df['price'] * df['number']
    return df


def discount(df: pd.DataFrame):
    dfa = df.copy()
    dfa.loc[df['number'] > 2, 'cost'] *= 0.5
    return dfa


if __name__ == '__main__':
    products = ['bread', 'milk', 'soda', 'cream']
    prices = [37, 58, 99, 72]
    price_list = pd.Series(prices, products)
    result = cheque(price_list, soda=3, milk=2, cream=1)
    with_discount = discount(result)
    print(result)
    print(with_discount)
