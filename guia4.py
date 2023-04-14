import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

N=100
S=np.random.normal(size=N)
H=np.random.normal(loc=0.5*S,size=N)

D=np.random.binomial(n=1, p=0.5, size=N)
Hstar=H.copy()
Hstar[D==1]=np.nan

#plt.plot(S, H, c="green", alpha=0.8, linewidth=2)
plt.scatter(S, Hstar, c="blue", linewidth=2)
plt.show