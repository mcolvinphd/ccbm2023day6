import pandas as pd
from matplotlib import pyplot as plt
import statsmodels.formula.api as smf
dat=pd.read_table("cal_sodium.txt",delimiter=' ')
res = smf.ols(formula='Calories ~ Sodium', data=dat).fit()
print(res.params)
print(res.summary())
plt.scatter(dat.Sodium,dat.Calories)
plt.plot(dat.Sodium,res.params[1]*dat.Sodium+res.params[0])
plt.savefig('Cal_Sodium.png',transparent=True)
plt.show()
