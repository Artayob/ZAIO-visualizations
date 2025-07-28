import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.random.randn(100)
y = np.random.randn(100)
colors = np.random.rand(100)
sizes = 500 * np.random.rand(100)

plt.scatter(x, y, 
            c=colors,
            s=sizes,
            alpha = 0.5,
            cmap='plasma'
            )
plt.colorbar()
plt.show()

print(pd.DataFrame(zip(x, y, colors, sizes)))