import pandas as pd


def update(df: pd.DataFrame):
    dfa = df.copy()
    dfa['average'] = dfa.mean(axis=1, numeric_only=True)
    return dfa.sort_values(['average', 'name'], ascending=[False, True])


if __name__ == '__main__':
    columns = ['name', 'maths', 'physics', 'computer science']
    data = {
        'name': ['Иванов', 'Петров', 'Сидоров', 'Васечкин', 'Николаев'],
        'maths': [5, 4, 5, 2, 4],
        'physics': [4, 4, 4, 5, 5],
        'computer science': [5, 2, 5, 4, 3]
    }
    journal = pd.DataFrame(data, columns=columns)
    filtered = update(journal)
    print(journal)
    print(filtered)
