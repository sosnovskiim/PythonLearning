import pandas as pd


def best(df: pd.DataFrame):
    return df[(df['maths'] >= 4) & (df['physics'] >= 4) & (df['computer science'] >= 4)]


if __name__ == '__main__':
    columns = ['name', 'maths', 'physics', 'computer science']
    data = {
        'name': ['Иванов', 'Петров', 'Сидоров', 'Васечкин', 'Николаев'],
        'maths': [5, 4, 5, 2, 4],
        'physics': [4, 4, 4, 5, 5],
        'computer science': [5, 2, 5, 4, 3]
    }
    journal = pd.DataFrame(data, columns=columns)
    filtered = best(journal)
    print(journal)
    print(filtered)
