import matplotlib.pyplot as plt
import numpy as np

def f(x, y):
    return np.sin(x) ** 10 + np.cos(10 + y * x) * np.cos(x)

x = np.linspace(0, 5, 100)
y = np.linspace(0, 5, 100)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)

plt.contour(X, Y, Z, colors='blue')
plt.show()

#Another contour plot 
plt.contour(X, Y, Z, cmap='RdGy')
plt.colorbar()
plt.show()

#Another contour plot SMOOTH CONTOUR PLOT
plt.imshow(Z, extent=[0, 5, 0, 5], origin='lower', cmap='RdGy', alpha= 0.8)
plt.colorbar()
plt.show()