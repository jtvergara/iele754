
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.arima.model import ARIMA


# Load CSV file
df = pd.read_excel('last_uci.xlsx')
print(df.head())

val_falta=df.isnull().sum()
print(val_falta)

df_limpio=df.dropna()
#cabe destacar que las columnas ya están en formato de fecha


traspuesto=df_limpio.transpose()
print(traspuesto)
traspuesto.columns=traspuesto.iloc[0]
traspuesto=traspuesto[1:]

traspuesto= traspuesto.rename(columns={'index':'fecha'})


traspuesto['fecha']=pd.to_datetime(traspuesto['fecha'], format='%d-%m-%Y')

valor_medio=traspuesto['total'].mean()
print(valor_medio)

plt.hist(traspuesto['total'])
plt.show()

correlacion = traspuesto['total'].corr(traspuesto['total'].astype(float))

traspuesto.plot(x='total', y='XII Región de Magallanes y de la Antártica Chilena')
plt.show()


# Descompone una columna de series temporales
descomposicion = seasonal_decompose(traspuesto['total'],
                                    model='additive', period=1)
descomposicion.plot()
plt.show()


# Crea y ajusta un modelo ARIMA
modelo = ARIMA(traspuesto['total'], order=(5,1,0))
modelo_ajustado = modelo.fit

#



