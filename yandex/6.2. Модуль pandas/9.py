import pandas as pd

xtl, ytl = map(int, input().split())
xbr, ybr = map(int, input().split())
df = pd.read_csv('data.csv')
print(df[(df['x'] >= xtl) & (df['y'] <= ytl) & (df['x'] <= xbr) & (df['y'] >= ybr)])
