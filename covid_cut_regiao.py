import pandas as pd

df = pd.read_csv('data/covid_hist.csv', sep=';')

for regiao in df['regiao'].drop_duplicates().values:
    df[df['regiao'] == regiao].to_csv(
        f'data/covid_hist_{regiao.lower()}.csv', index=False, sep=';')
