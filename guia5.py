#Generar codigo de https://www.youtube.com/watch?v=uial-2girHQ&t=38s

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats


data_uniforme=stats.uniform.rvs(size=10000,loc=0,scale=10) #genera datos uniformes random desde 0 a 10
pd.DataFrame(data_uniforme).plot(kind='density', figsize=(9,9), xlim=(-5,15))
stats.uniform.cdf(x=2.5, loc=0, scale=10) #nos dice que hay un 25% de probabilidad que el valor caiga debajo de 2.5
stats.uniform.ppf(q=0.4, loc=0, scale=10) #nos dice el valor que toma el eje x para sacar el 40% de los valores hacia la izquierda

for x in range(-1,12,2): #hacemos un for para sacar la densidad de los valores dentro del rango
    print("densidad en valor de x" + str(x))
    print( stats.uniform.pdf(x, loc=0, scale=10))

import random
random.randint(0,10)
random.choice([2,3,4,5,6,7,8])
random.random()
random.uniform(0,10)

random.seed(12)
print([random.uniform(0,10) for x in range(4)])

# plotear areas de distribuciones normales

plt.rcParams["figure.figsize"]=(7,7)

plt.fill_between(x=np.arange(-4,-1,0.01),y1=stats.norm.pdf(np.arange(-4,-1,0.01)), facecolor='orange', alpha=0.35)
plt.fill_between(x=np.arange(1,4,0.01),y1=stats.norm.pdf(np.arange(1,4,0.01)), facecolor='orange', alpha=0.35)
plt.fill_between(x=np.arange(-1,1,0.01),y1=stats.norm.pdf(np.arange(-1,1,0.01)), facecolor='blue', alpha=0.35)

plt.text(x=-1.8, y=0.03, s=round(prob_under_minus1, 3))
plt.text(x=-0.2, y=0.03, s=round(between_prob, 3))
plt.text(x=1.4, y=0.03, s=round(prob_over_1, 3))

print(stats.norm.ppf(q=0.025)) #encuentra el valor en x para el 2.5% de los valores a la izquierda
print(stats.norm.ppf(q=0.975)) #lo mismo pero para el cuantil de la derecha

print(stats.norm.cdf(x=-1)) #cuantos datos hay debajo de -1
print(stats.norm.cdf(x=1)) #cuantos datos hay sobre 1 (en eje x)

#%%

##### Ahora veremos distribucion normal
#nos dice: cuan probable es de obtener un numero dado de aciertos en endtrail 

coin_flip=stats.binom.rvs(n=10,p=0.5,size=1000) #de 1000 intentos, con prob 0.5 y diez tiros de los mil intentos, se obtiene lo siguiente 
print(pd.crosstab(index="counts", columns=coin_flip))
pd.DataFrame(coin_flip).hist(range=(-0.5,10.5), bins=11); #pedimos ploteo en un histograma
#notar que solo 2 veces obtuvimos cero caras de la moneda, osea un 0.2% de probabilidad de ocurrencia (creo)
#notar que como son valores discretos, el histograma lo plotea bien y aun asi se puede nota la campana

#ahora usemos una moneda cargada en 0.8 para obtener cara (quizas modelar un basquetbolista lanzando tirolibres)
coin_flip=stats.binom.rvs(n=10,p=0.8,size=1000) #ahora con 80% de acierto
print(pd.crosstab(index="counts", columns=coin_flip))
pd.DataFrame(coin_flip).hist(range=(-0.5,10.5), bins=11);
#con 1000 intentos, nunca hubo 0 sellos, debido a la carga que le dimos a la moneda

#con .cdf podemos ver la probabilidad de obtener debajo de x cantidad de caras
stats.binom.cdf(k=5, n=10, p=0.8) #pedimos la probabilidad de obtener 5 aciertos (caras)
1-stats.binom.cdf(k=5, n=10, p=0.8) #pedimos la probabilidad de obtener 5 aciertos (caras)


# %%
#ahora veremos la geometrica y exponencial.

random.seed(12)
flips_till_heads=stats.geom.rvs(size=100, p=0.5)
print(pd.crosstab(index="counts", columns=flips_till_heads))
pd.DataFrame(flips_till_heads).hist(range=(-0.5, max(flips_till_heads + 0.5), bins:=max(flips_till_heads)+1))

first_five = stats.geom.cdf(k=5, p=0.5)

#plotear la distribucion exponencial
plt.fill_between(x=np.arange(0,1,0.01), y1=stats.expon.pdf(np.arange(0,1,0.01)), facecolor='blue', alpha=0.35)
plt.fill_between(x=np.arange(1,7,0.01), y1=stats.expon.pdf(np.arange(1,7,0.01)), facecolor='red', alpha=0.35)

#plt.text(x=0.3, y=0.2, s=round(prob_1,3))
#plt.text(x=1.5, y=0.08, s=round(1-prob_1,3));


# %%
#poission distribution

#random.seed(12)
arrival_rate_1=stats.poisson.rvs(size=10000, mu=1)
print(pd.crosstab(index='counts', columns=arrival_rate_1))
pd.DataFrame(arrival_rate_1).hist(range=(-0.5, max(arrival_rate_1)+0.5), bins=max(arrival_rate_1)+1);

#random.seed(12)
arrival_rate_1=stats.poisson.rvs(size=10000, mu=10)#ahora con mas arrivals por time
print(pd.crosstab(index='counts', columns=arrival_rate_1))
pd.DataFrame(arrival_rate_1).hist(range=(-0.5, max(arrival_rate_1)+0.5), bins=max(arrival_rate_1)+1);




# %%
import csv

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











# %%
