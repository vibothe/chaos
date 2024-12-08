import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Parameters
a = 0.1  # Natural growth rate of rabbits
b = 0.02  # Death rate of rabbits due to predation
c = 0.1  # Natural death rate of wolves
d = 0.01  # Growth rate of wolves per rabbit eaten

# Time points
t = np.linspace(0, 200, 10000)

# Initial populations: 40 rabbits and 9 wolves
initial_conditions = [40, 9]

# Lotka-Volterra equations
def lotka_volterra(y, t, a, b, c, d):
    R, W = y
    dRdt = a * R - b * R * W
    dWdt = -c * W + d * R * W
    return [dRdt, dWdt]

# Solve ODE
solution = odeint(lotka_volterra, initial_conditions, t, args=(a, b, c, d))
R, W = solution.T

# Plot results
plt.figure(figsize=(12, 8))

# Plot populations over time
plt.subplot(2, 1, 1)
plt.plot(t, R, label='Rabbits')
plt.plot(t, W, label='Wolves')
plt.xlabel('Time')
plt.ylabel('Population')
plt.title('Rabbit and Wolf Population Over Time')
plt.legend()
plt.grid()

# Plot phase space (Rabbits vs Wolves)
plt.subplot(2, 1, 2)
plt.plot(R, W, color='purple')
plt.xlabel('Rabbits')
plt.ylabel('Wolves')
plt.title('Phase Space: Rabbits vs Wolves')
plt.grid()

plt.tight_layout()
plt.show()
