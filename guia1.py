#Guia 1: se trata de analisis de temperatura

import pandas as pd 
import seaborn as sns

df = pd.read_csv("/Users/jtvergara/iele754/2023_temperatura_aire_ceaza.csv") 

print(df.head()) 

df["time"] = pd.to_datetime(df.time, format= "%Y-%m-%d %H:%M:%S") 
df1 = df.loc[(df["time"].dt.month==3)] 
print(df1)



df2 = pd.read_csv("/Users/jtvergara/iele754/2020_temperatura_aire_ceaza.csv")
df2["time"] = pd.to_datetime(df2.time, format= "%Y-%m-%d %H:%M:%S")
df3 = df2.loc[(df2["time"].dt.month==3)]

print(df3)

sns.kdeplot(df1.prom)
sns.kdeplot(df3.prom)