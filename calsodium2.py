import pandas as pd
from matplotlib import pyplot as plt
import statsmodels.formula.api as smf
dat=pd.read_table("cal_sodium.txt",delimiter=' ')
res = smf.ols(formula='Calories ~ Type', data=dat).fit()
print(res.params)
print(res.summary())
plt.scatter(dat.Calories,dat.Type)
plt.savefig('Cal_Type.png',transparent=True)
plt.show()
