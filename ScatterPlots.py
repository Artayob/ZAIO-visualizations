import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 20)
y = np.sin(x)

plt.plot(x, y, '^k')
plt.ylim(-1.5, 1.5)
plt.xlim(-2, 12)
plt.show()

print("-----------------------------------------------------------")

x = np.linspace(0, 10, 20)
y = np.sin(x)

plt.plot(x, y, '-p',                # Plot pentagon (Marker) at points
         color = 'red',             # red colored line 
         markersize = 10,           # Marker size
         markerfacecolor = 'green', # Marjer body/ face color
         markeredgecolor = 'blue',  # Marker border color
         markeredgewidth = 1        # Marker edge width 
         )

plt.ylim(-1.5, 1.5)
plt.show()

# Plotting scatter plots using plt.scatter 

plt.scatter(x, y, marker='o', alpha=0.5)
plt.title("Scatter plot using Scatter Method")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.show()