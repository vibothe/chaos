import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

def julia_set(width, height, x_min, x_max, y_min, y_max, c, max_iter):
    x = np.linspace(x_min, x_max, width)
    y = np.linspace(y_min, y_max, height)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y
    div_time = np.zeros(Z.shape, dtype=int)
    M = np.full(Z.shape, True, dtype=bool)

    for i in range(max_iter):
        Z[M] = Z[M]**2 + c
        M[np.abs(Z) > 2] = False
        div_time[M & (div_time == 0)] = i

    return div_time

# Parameters
width, height = 800, 800
x_min, x_max = -1.5, 1.5
y_min, y_max = -1.5, 1.5
c = complex(-0.7, 0.27015)
max_iter = 256

# Generate Julia Set
julia = julia_set(width, height, x_min, x_max, y_min, y_max, c, max_iter)

# Custom colormap
colors = ["#000764", "#206bcb", "#edffff", "#ffaa00", "#000200"]
cmap = LinearSegmentedColormap.from_list("custom_cmap", colors, N=256)

# Plotting
plt.figure(figsize=(10, 10))
plt.imshow(julia, extent=[x_min, x_max, y_min, y_max], cmap=cmap, interpolation='bilinear')
plt.colorbar(label='Number of iterations', orientation='vertical')
plt.title('Julia Set for c = -0.7 + 0.27015i', fontsize=18, fontweight='bold')
plt.xlabel('Re(z)')
plt.ylabel('Im(z)')
plt.show()
