import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

X = np.random.rand(100)
Y = X + np.random.rand(100) * 0.1

X_const = sm.add_constant(X)

model = sm.OLS(Y, X_const)
results = model.fit()
print(results.summary())

plt.scatter(X, Y)

X_plot = np.linspace(0,1,100)
plt.plot(X, X * results.params[1] + results.params[0])
plt.show()
