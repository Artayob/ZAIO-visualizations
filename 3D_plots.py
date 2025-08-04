import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from mpl_toolkits import mplot3d

# plt.style.use('seaborn-whitegrid')
# fig = plt.figure()
# ax = plt.axes(projection='3d')
# plt.show()

# plt.style.use('classic')
sns.set_style('whitegrid')
fig = plt.figure()
ax= plt.axes(projection='3d')
radius = 2
c = 3

theta = np.linspace(-12, 12, 100)
x = radius * np.sin(theta)
y = radius * np.cos(theta)
z = c * theta

ax.plot3D(x, y, z)
plt.show()

# 3D scatter plot 
sns.set_style('whitegrid')
fig = plt.figure()
ax= plt.axes(projection='3d')

x = np.random.randn(100)
y = np.random.randn(100)
z = np.random.randn(100)

ax.scatter(x, y, z, c=z, cmap='Greens')
ax.set(xlabel='X-axis', ylabel='Y-axis', zlabel='Z-axis')
plt.show()

# 3D contour plot 
def f(x, y):
    return np.sin(np.sqrt(x **2 + y **2))

x = np.linspace(-6, 6, 30)
y = np.linspace(-6, 6, 30)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)

plt.figure()
ax = plt.axes(projection= '3d')
ax.contour3D(X, Y, Z, 50, cmap='Greens')

ax.set(xlabel='X axis', ylabel = 'Y axis', zlabel= 'Z axis')
plt.show()