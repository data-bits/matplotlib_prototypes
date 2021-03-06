import numpy as np
import matplotlib.pyplot as plt

r = 3 * np.pi * np.random.random(1000)
theta = 5 * np.pi * np.random.random(1000)
xdata = np.ravel(r * np.sin(theta))
ydata = np.ravel(r * np.cos(theta))
zdata = np.sin(xdata) + np.cos(ydata)

fig = plt.figure(figsize=(9, 6))
ax = plt.axes(projection = '3d')

ax.plot_trisurf(xdata, ydata, zdata, cmap = 'inferno')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

ax.view_init(40, 100)

plt.show()
