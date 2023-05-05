import matplotlib.pyplot as plt
import scipy.stats
import csv
import numpy as np
import pandas as pd
df=pd.read_csv("Covid-19.csv")
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


data=[]
#with open("Covid-19.csv") as file:

#    reader=csv.reader(file, delimiter=',')
#    for row in reader:
#        data.append(float(row(0)))

plt.hist(data, bins=100, density=True)

[mean_fit, std_fit]=scipy.stats.norm.fit(data)

print(mean_fit)
print(std_fit)


plt.show