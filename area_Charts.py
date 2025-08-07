import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np

datadict = {'Total Daily Infection': [1326, 1456, 1794, 1712, 1634, 1565],
            'Vaccine Jab 1' : [651, 670, 710, 736, 722, 768],
            'Vaccine Jab 2' : [322, 341, 361, 383, 399, 404]}

df = pd.DataFrame(datadict, index=pd.date_range(start='2021/04/01', end='2021/04/06', freq = 'D'))

ax = df.plot.area()
plt.legend(loc='upper left')
plt.ylim(0, 4000)
plt.show()

# Overlapping area charts 
datadict = {'Total Daily Infection': [1326, 1456, 1794, 1712, 1634, 1565],
            'Vaccine Jab 1' : [651, 670, 710, 736, 722, 768],
            'Vaccine Jab 2' : [322, 341, 361, 383, 399, 404]}
df = pd.DataFrame(datadict, index=pd.date_range(start='2021/04/01', end='2021/04/06', freq = 'D'))

ax = df.plot.area(stacked=False)
plt.legend(loc='upper left')
plt.ylim(0, 2500)
plt.show()