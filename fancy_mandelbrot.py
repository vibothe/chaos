import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    z = 0
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

# Parameters for the plot
width, height = 800, 800
x_min, x_max = -2.0, 1.0
y_min, y_max = -1.5, 1.5
max_iter = 1000

# Create a grid of complex numbers
x = np.linspace(x_min, x_max, width)
y = np.linspace(y_min, y_max, height)
X, Y = np.meshgrid(x, y)
C = X + 1j * Y

# Apply the mandelbrot function to each point in the grid using vectorization
mandelbrot_set = np.zeros(C.shape, dtype=int)
for i in range(width):
    for j in range(height):
        mandelbrot_set[j, i] = mandelbrot(C[j, i], max_iter)

# Normalize the values for coloring
norm_mandelbrot_set = mandelbrot_set / mandelbrot_set.max()

# Fancy plotting of the Mandelbrot set
plt.figure(figsize=(10, 10))

# Use a colormap for better visualization
plt.imshow(norm_mandelbrot_set, extent=[x_min, x_max, y_min, y_max], cmap='inferno', interpolation='bilinear')

# Add a color bar
cbar = plt.colorbar()
cbar.set_label('Number of iterations', rotation=270, labelpad=15)

# Add labels and title
plt.title('Mandelbrot Set', fontsize=18, fontweight='bold')
plt.xlabel('Re(c)')
plt.ylabel('Im(c)')

# Add grid lines for better visualization
plt.grid(color='white', linestyle='--', linewidth=0.5)

plt.show()
