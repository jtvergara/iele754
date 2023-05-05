#Guia 4: tutorial de ajustar distribuciones en python (traduccion R a python)


import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import bernoulli,norm
#%%

N=100
##S=np.random.normal(size=N)
S=norm(0,1).rvs(size=N)
H=norm(0,0.5*abs(S)).rvs(size=N)
#H=norm(0,0.5*S)
sns.scatterplot(S)
sns.scatterplot(H)
D=np.random.binomial(n=1, p=0.5, size=N)
Hstar=H.copy()
Hstar[D==1]=np.nan

plt.hist(S,H)
[mean_fit, std_fit]=scipy
#plt.plot(S, H, c="green", alpha=0.8, linewidth=2)
#plt.scatter(S, Hstar, c="blue", linewidth=2)
#plt.show()    

