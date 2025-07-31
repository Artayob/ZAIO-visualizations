import matplotlib.pyplot as plt
import numpy as np
ax1 = plt.subplot(2,3,1)
ax2 = plt.subplot(2,3,2)
ax3 = plt.subplot(2,3,3)
ax4 = plt.subplot(2,3,4)
ax5 = plt.subplot(2,3,5)
ax6 = plt.subplot(2,3,6)

print(ax1, ax2, ax3, ax4, ax5, ax6)

n_rows = 2
n_cols = 2
fig, axes = plt.subplots(n_rows, n_cols)
for row_num in range(n_cols):
    for col_num in range(n_cols):
        ax = axes[row_num][col_num]
        ax.plot(np.random.rand(20))
        ax.set_title(f'Plot ({row_num+1}, {col_num+1})')

fig.suptitle('Main title')
fig.tight_layout()
plt.show()
