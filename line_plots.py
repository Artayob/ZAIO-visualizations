import matplotlib.pyplot as plt
import numpy as np

x = [1,2,3,4]
y =[3,4,5,6]
plt.subplot(2,1,1)
plt.plot(x,y)
plt.show()

print("----------------------------------------------------------------------------------------------")

x = [1,2,3,4]
y = [3,4,5,6]
fig, ax = plt.subplots(2)
ax[0].plot(x,y)
ax[1].plot(x,y)
plt.show()

print("----------------------------------------------------------------------------------------------")

x = np.linspace(0, 10, 100)
print(x)

fig = plt.figure()
plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))
plt.show()

print("------------------------------------------------------------------------------------------------")

fig = plt.figure()
plt.plot(x, np.sin(x), '-')
plt.plot(x, np.cos(x), '--')
plt.show()
print("Dashed line plot")
print("------------------------------------------------------------------------------------------------")

fig.savefig('myfirst_fig.png')

from IPython.display import Image
print(Image('myfirst_fig.png'))

print("------------------------------------------------------------------------------------------------")

plt.figure()
x = np.arange(0., 10., 0.2)
print(x)
y = 4*x*x +3
plt.figure(figsize=(7,5))
plt.plot(x, y)
plt.grid(True)
plt.show()