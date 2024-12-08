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
max_iter = 256

# Create a grid of complex numbers
x = np.linspace(x_min, x_max, width)
y = np.linspace(y_min, y_max, height)
X, Y = np.meshgrid(x, y)
C = X + 1j * Y

# Apply the mandelbrot function to each point in the grid
mandelbrot_set = np.zeros(C.shape, dtype=int)
for i in range(width):
    for j in range(height):
        mandelbrot_set[j, i] = mandelbrot(C[j, i], max_iter)

# Plot the results
plt.figure(figsize=(10, 10))
plt.imshow(mandelbrot_set, extent=[x_min, x_max, y_min, y_max], cmap='hot')
plt.colorbar(label='Number of iterations')
plt.title('Mandelbrot Set')
plt.xlabel('Re(c)')
plt.ylabel('Im(c)')
plt.show()
