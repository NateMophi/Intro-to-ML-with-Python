import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import random

# 3D
ax = plt.axes(projection = "3d")
# x = np.random.random(100)
# y = np.random.random(100)
# z = np.random.random(100)

# ax.scatter(x, y, z)
# ax.set_title("3D plot")
# ax.set_xlabel("test")
# ax.set_ylabel("test")
# ax.set_zlabel("test")
# plt.show()

# x = np.arange(0,50, 0.1)
# y = np.arange(0,50, 0.1)
# z = np.cos(x+y)

# ax.plot(x, y, z)
# ax.set_title("3D plot")
# ax.set_xlabel("values")
# ax.set_ylabel("Sine")
# ax.set_zlabel("Cosine")
# plt.show()

# # MESH GRID
# x = np.arange(-5,5,0.1)
# y = np.arange(-5,5,0.1)
# X,Y = np.meshgrid(x,y)
# Z=np.sin(X)*np.cos(Y)
# ax.plot_surface(X,Y,Z, cmap = "Spectral")
# ax.view_init(azim=0, elev=90)
# plt.show()
 

# ANIMATIONS
# heads_tails = [0,0]
# for _ in range(100000):
#     heads_tails[random.randint(0,1)]+=1
#     plt.bar(["Heads", "Tails"], heads_tails, color=["red", "blue"])
#     plt.pause(0.01)
# plt.show()
