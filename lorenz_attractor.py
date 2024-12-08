import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Lorenz system parameters
sigma = 10.0
rho = 28.0
beta = 8.0 / 3.0

# Time parameters
dt = 0.01
num_steps = 10000

# Initialize arrays
xs = np.empty(num_steps + 1)
ys = np.empty(num_steps + 1)
zs = np.empty(num_steps + 1)

# Initial conditions
xs[0], ys[0], zs[0] = 0.0, 1.0, 1.05

# Euler method to solve the Lorenz system
for i in range(num_steps):
    x_dot = sigma * (ys[i] - xs[i])
    y_dot = xs[i] * (rho - zs[i]) - ys[i]
    z_dot = xs[i] * ys[i] - beta * zs[i]
    xs[i + 1] = xs[i] + x_dot * dt
    ys[i + 1] = ys[i] + y_dot * dt
    zs[i + 1] = zs[i] + z_dot * dt

# Plotting the Lorenz attractor
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(xs, ys, zs, lw=0.5)
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
plt.show()
