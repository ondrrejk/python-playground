import numpy as np
import matplotlib.pyplot as plt

# Parametry
v0 = 30            # počáteční rychlost (m/s)
theta = 45         # úhel (stupně)
g = 9.81           # tíhové zrychlení

# Převod úhlu na radiany
theta_rad = np.radians(theta)

# Rozklad rychlosti
v0x = v0 * np.cos(theta_rad)
v0y = v0 * np.sin(theta_rad)

# Časová osa
t = np.linspace(0, 2 * v0y / g, 300)

# Trajektorie
x = v0x * t
y = v0y * t - 0.5 * g * t**2

# Graf
plt.figure(figsize=(10, 5))
plt.plot(x, y, label="Trajektorie")
plt.title("Vrh šikmý bez odporu vzduchu")
plt.xlabel("Vzdálenost (m)")
plt.ylabel("Výška (m)")
plt.grid(True)
plt.legend()
plt.show()
