import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1, 10, 30)
err = np.random.rand(30) * 70
y = 5*x*x + 5

plt.errorbar(x, y, yerr = err, fmt = 'ok', ecolor= 'red')
plt.show()