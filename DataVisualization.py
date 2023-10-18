import numpy as np
from sklearn.datasets import make_moons
import matplotlib.pyplot as plt


x = np.linspace(0, 9, 100)
y = np.linspace(10, 19, 100)



x,y = np.meshgrid(x,y)
z = np.sin(x) + np.sin(y)


ax = plt.axes(projection='3d')
ax.plot_surface(x, y, z, color='b')
plt.show()