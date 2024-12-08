import matplotlib.pyplot as plt
import numpy as np

def sierpinski_triangle(ax, vertices, depth):
    if depth == 0:
        triangle = plt.Polygon(vertices, edgecolor='black', fill=True, facecolor='white')
        ax.add_patch(triangle)
    else:
        midpoints = [
            (vertices[0] + vertices[1]) / 2,
            (vertices[1] + vertices[2]) / 2,
            (vertices[2] + vertices[0]) / 2
        ]
        
        sierpinski_triangle(ax, [vertices[0], midpoints[0], midpoints[2]], depth - 1)
        sierpinski_triangle(ax, [vertices[1], midpoints[0], midpoints[1]], depth - 1)
        sierpinski_triangle(ax, [vertices[2], midpoints[1], midpoints[2]], depth - 1)

# Plot parameters
fig, ax = plt.subplots()
ax.set_aspect('equal')

# Define the initial triangle vertices
initial_vertices = np.array([[0, 0], [1, np.sqrt(3)], [2, 0]])

# Recursion depth
depth = 6

# Draw the Sierpinski triangle
sierpinski_triangle(ax, initial_vertices, depth)

# Remove axes
ax.axis('off')

# Display the plot
plt.show()
