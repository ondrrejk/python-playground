import numpy as np
import matplotlib.pyplot as plt

# Parametry tělesa a prostředí
m = 80               # hmotnost (kg)
Cd = 1.0             # koeficient odporu (bezrozměrný)
A = 0.7              # čelní plocha (m^2)
rho = 1.225          # hustota vzduchu (kg/m^3)
g = 9.81             # tíhové zrychlení

# Počáteční podmínky
y = 1000             # výška (m)
v = 0                # počáteční rychlost (m/s)
dt = 0.01            # krok simulace

# Uložení dat
ys = []
vs = []
ts = []

t = 0

while y > 0:
    ys.append(y)
    vs.append(v)
    ts.append(t)

    # Odpor vzduchu
    Fd = 0.5 * Cd * rho * A * v**2

    # Směr odporu (proti pohybu)
    if v > 0:
        Fd = Fd
    else:
        Fd = -Fd

    # Zrychlení
    a = g - Fd / m

    # Eulerova metoda
    v = v + a * dt
    y = y - v * dt
    t += dt

# Grafy
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(ts, ys)
plt.title("Výška v čase")
plt.xlabel("čas (s)")
plt.ylabel("výška (m)")
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(ts, vs)
plt.title("Rychlost v čase")
plt.xlabel("čas (s)")
plt.ylabel("rychlost (m/s)")
plt.grid(True)

plt.tight_layout()
plt.show()

print(f"Čas dopadu: {t:.2f} s")
print(f"Konečná rychlost: {v:.2f} m/s")
