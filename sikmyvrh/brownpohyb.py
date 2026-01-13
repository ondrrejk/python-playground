import numpy as np
import matplotlib.pyplot as plt

# Parametry simulace
N = 5000          # počet kroků
step_size = 1.0   # směrodatná odchylka kroku

# Generování náhodných kroků
dx = np.random.normal(0, step_size, N)
dy = np.random.normal(0, step_size, N)

# Výpočet trajektorie
x = np.cumsum(dx)
y = np.cumsum(dy)

# Vykreslení
plt.figure(figsize=(8, 8))
plt.plot(x, y, linewidth=1)
plt.scatter([x[0]], [y[0]], color='green', label="Start")
plt.scatter([x[-1]], [y[-1]], color='red', label="Konec")

plt.title("2D Brownův pohyb")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.show()
