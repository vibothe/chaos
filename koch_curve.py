import matplotlib.pyplot as plt
import numpy as np

def koch_curve(ax, x1, y1, x2, y2, depth):
    if depth == 0:
        ax.plot([x1, x2], [y1, y2], color='blue', lw=2)
    else:
        # Calculate new points
        dx = x2 - x1
        dy = y2 - y1
        
        # Calculate 1/3 and 2/3 points
        x1_new = x1 + dx / 3
        y1_new = y1 + dy / 3
        x3 = x1 + 2 * dx / 3
        y3 = y1 + 2 * dy / 3
        
        # Calculate peak of the equilateral triangle
        height = np.sqrt(3) * dx / 6
        x2_new = (x1 + x2) / 2
        y2_new = (y1 + y2) / 2 + height
        
        # Recursively draw segments
        koch_curve(ax, x1, y1, x1_new, y1_new, depth - 1)
        koch_curve(ax, x1_new, y1_new, x2_new, y2_new, depth - 1)
        koch_curve(ax, x2_new, y2_new, x3, y3, depth - 1)
        koch_curve(ax, x3, y3, x2, y2, depth - 1)

# Plot parameters
fig, ax = plt.subplots(figsize=(8, 6))

# Initial segment
x1, y1 = 0, 0
x2, y2 = 1, 0

# Depth of recursion (adjust as desired)
depth = 4

# Plot the Koch curve
koch_curve(ax, x1, y1, x2, y2, depth)

# Adjust plot limits and labels
ax.set_xlim(-0.1, 1.1)
ax.set_ylim(-0.1, 0.5)
ax.set_aspect('equal')
ax.axis('off')
plt.title(f'Koch Curve (depth = {depth})', fontsize=16)

plt.show()
