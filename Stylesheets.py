import numpy as np 
import matplotlib as mpl
import matplotlib.pyplot as plt

x = np.linspace(0,1,1000)
y = x*x

mpl.rcParams['lines.linewidth'] = 5
mpl.rcParams['lines.linestyle'] = '-'
plt.plot(x, y)
plt.show()

print(plt.rcParams)

# Turning off the grid
plt.rcParams["axes.grid"] = False

x = np.linspace(0,1,1000)
y = x*x

mpl.rcParams['lines.linewidth'] = 5
mpl.rcParams['lines.linestyle'] = '-'
plt.plot(x, y)
plt.show()

# Use my own stylesheet
plt.style.use('mystyle.mplstyle')

# Display my style sheet

# stylefile = open("mystyle.mplstyle")
# lines = stylefile.readlines()
# print(lines)

