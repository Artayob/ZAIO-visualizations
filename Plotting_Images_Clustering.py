import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
digits = load_digits(n_class=10)

fig, ax= plt.subplots(8,8, figsize=(10, 10))
for i, axi in enumerate(ax.flat):
    #print(digits.images[1])
    axi.imshow(digits.images[i], cmap='binary')
    axi.set(xticks=[], yticks=[])

plt.show()

from sklearn.manifold import Isomap
iso = Isomap(n_components=2)
projection = iso.fit_transform(digits.data)

plt.scatter(projection[:,0], projection[:,1],
            c=digits.target, cmap="viridis")
plt.colorbar(ticks=range(10), label='Digits Value')
plt.clim(-0.5, 5.5)
plt.show()