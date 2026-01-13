import numpy as np
import matplotlib.pyplot as plt

# Parametry systému
m = 1.0       # hmotnost (kg)
k = 10.0      # tuhost pružiny (N/m)
x = 1.0       # počáteční výchylka (m)
v = 0.0       # počáteční rychlost (m/s)
dt = 0.001    # krok simulace
T = 10        # celkový čas simulace (s)

# Uložení dat
xs = []
vs = []
ts = []
Es = []

t = 0

while t < T:
    # Uložení
    xs.append(x)
    vs.append(v)
    ts.append(t)

    # Energie
    Ek = 0.5 * m * v**2
    Ep = 0.5 * k * x**2
    Es.append(Ek + Ep)

    # Zrychlení
    a = -(k/m) * x

    # Eulerova metoda
    v = v + a * dt
    x = x + v * dt

    t += dt

# Grafy
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(ts, xs)
plt.title("Poloha x(t)")
plt.ylabel("x (m)")
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(ts, vs)
plt.title("Rychlost v(t)")
plt.ylabel("v (m/s)")
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(ts, Es)
plt.title("Celková energie E(t)")
plt.xlabel("čas (s)")
plt.ylabel("E (J)")
plt.grid(True)

plt.tight_layout()
plt.show()
