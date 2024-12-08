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

# Runge-Kutta 4th order method to solve the Lorenz system
for i in range(num_steps):
    x, y, z = xs[i], ys[i], zs[i]
    
    kx1 = sigma * (y - x)
    ky1 = x * (rho - z) - y
    kz1 = x * y - beta * z
    
    kx2 = sigma * (y + 0.5*ky1*dt - (x + 0.5*kx1*dt))
    ky2 = (x + 0.5*kx1*dt) * (rho - (z + 0.5*kz1*dt)) - (y + 0.5*ky1*dt)
    kz2 = (x + 0.5*kx1*dt) * (y + 0.5*ky1*dt) - beta * (z + 0.5*kz1*dt)
    
    kx3 = sigma * (y + 0.5*ky2*dt - (x + 0.5*kx2*dt))
    ky3 = (x + 0.5*kx2*dt) * (rho - (z + 0.5*kz2*dt)) - (y + 0.5*ky2*dt)
    kz3 = (x + 0.5*kx2*dt) * (y + 0.5*ky2*dt) - beta * (z + 0.5*kz2*dt)
    
    kx4 = sigma * (y + ky3*dt - (x + kx3*dt))
    ky4 = (x + kx3*dt) * (rho - (z + kz3*dt)) - (y + ky3*dt)
    kz4 = (x + kx3*dt) * (y + ky3*dt) - beta * (z + kz3*dt)
    
    xs[i+1] = x + (kx1 + 2*kx2 + 2*kx3 + kx4) * dt / 6
    ys[i+1] = y + (ky1 + 2*ky2 + 2*ky3 + ky4) * dt / 6
    zs[i+1] = z + (kz1 + 2*kz2 + 2*kz3 + kz4) * dt / 6

# Fancy plotting of the Lorenz attractor
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Color mapping based on time steps
colors = plt.cm.viridis(np.linspace(0, 1, num_steps + 1))

for i in range(num_steps):
    ax.plot(xs[i:i+2], ys[i:i+2], zs[i:i+2], color=colors[i], lw=0.5)

ax.set_title("Lorenz Attractor", fontsize=18, fontweight='bold')
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_facecolor('black')  # Background color
ax.xaxis.label.set_color('white')
ax.yaxis.label.set_color('white')
ax.zaxis.label.set_color('white')
ax.tick_params(colors='white')
ax.w_xaxis.line.set_color("white")
ax.w_yaxis.line.set_color("white")
ax.w_zaxis.line.set_color("white")
fig.patch.set_facecolor('black')

plt.show()
