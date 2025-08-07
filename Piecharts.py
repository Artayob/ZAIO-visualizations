import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np
import seaborn as sns

sns.set_style('dark')
x = [120000, 170000, 223000, 205000, 156000]

labels = ['Kansas', 'Montgomery', 'Marysville', 'Geargetown', 'Deoborn']

fig, ax = plt.subplots()
ax.pie(x, labels = labels, autopct='%.1f%%')
ax.set_title("Total Car Production across cities in the US")
plt.show()

#Exploding 
x = [12000, 17000, 22300, 20500, 15500]
labels = ['Kansas', 'Montgomery', 'Marysville', 'Geargetown', 'Deoborn']
colors = ['limegreen', 'lavender', 'seagreen', 'orange', 'yellow', 'black', 'red']

explode = [0, 0, 0, 0.1, 0]

fig, ax = plt.subplots()
ax.pie(x, labels = labels, colors= colors,  autopct='%.1f%%', explode= explode)
ax.set_title("Sales Proportions")
plt.show()

# Plotting the data values instead of percent, use startange 
x = [12000, 17000, 22300, 20500, 15500]
labels = ['Kansas', 'Montgomery', 'Marysville', 'Geargetown', 'Deoborn']
colors = ['limegreen', 'lavender', 'seagreen', 'orange', 'yellow', 'black', 'red']

explode = [0, 0, 0, 0.1, 0]
sumtot = sum(x)
def absolute_value(val):
    a = np.round(sumtot*val/100, 0)
    return a

fig, ax = plt.subplots()
ax.pie(x, labels = labels, colors= colors,  autopct=absolute_value, explode= explode, startangle=90)
ax.set_title("Survey responses", fontsize=15)
plt.show()
