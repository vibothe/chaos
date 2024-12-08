import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Parameters
r = 0.1  # Intrinsic growth rate
K = 100  # Carrying capacity

# Logistic growth equation
def logistic_growth(P, t, r, K):
    return r * P * (1 - P / K)

# Time points
t = np.linspace(0, 200, 1000)

# Initial population
P0 = 10

# Solve ODE
P = odeint(logistic_growth, P0, t, args=(r, K))

# Plot results
plt.figure(figsize=(10, 6))
plt.plot(t, P, label='Population')
plt.xlabel('Time')
plt.ylabel('Population Size')
plt.title('Logistic Growth')
plt.grid()
plt.legend()
plt.show()
