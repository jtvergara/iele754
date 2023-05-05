#Guia 2: Clean data covid and plot cases

import pandas as pd
import seaborn as sns

df=pd.read_csv('Covid-19.csv')
print(df.head())


vals = list(df.columns)[5:-1]
ids = list(df.columns)[:5]

df_tidy = pd.melt(df, value_vars=vals, id_vars=ids)
print(df_tidy)

df_tidy = df_tidy.dropna()
print(df_tidy)
df_tidy.info()

list(df_tidy.dtypes)
df_tidy['variable'] = pd.to_datetime(df_tidy['variable'])
df_tidy.dtypes
print(df_tidy)

df_tidy['variable'] = pd.to_datetime(df_tidy['variable'], format='%Y-%m-%d')
print(df_tidy.variable.dtypes)

df_tidy_meses=df_tidy[(df_tidy['variable']>='2020-03-01') & (df_tidy['variable']<='2020-06-30')]
#df_tidy_meses.sort_values(by='variable',ascending=False).tail()
df_tidy_meses_lobarnechea=df_tidy_meses[df_tidy_meses['Comuna']=='Lo Barnechea'].sort_values(by='variable')
df_tidy_meses_lobarnechea

weekly_df = df_tidy_meses_lobarnechea.groupby(pd.Grouper(key='variable', freq='W')).mean()
sns.lineplot(data=df_tidy_meses_lobarnechea,x='variable', y='value')
sns.lineplot(data=weekly_df,x='variable', y='value') 