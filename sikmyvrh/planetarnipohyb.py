import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ==========================
# Parametry simulace
# ==========================

G = 6.67430e-11        # gravitační konstanta (SI)
m1 = 1.989e30          # hmotnost tělesa 1 (např. "Slunce")
m2 = 5.972e24          # hmotnost tělesa 2 (např. "Země")

# Počáteční podmínky (2D)
# Zvolíme soustavu, kde těžiště je v počátku
# r1, r2 ... pozice; v1, v2 ... rychlosti

# Počáteční vzdálenost ~ 1 AU
r0 = 1.496e11  # m

# Vypočítáme počáteční polohy tak, aby těžiště bylo v (0, 0)
r1 = np.array([-m2 / (m1 + m2) * r0, 0.0])  # těleso 1
r2 = np.array([ m1 / (m1 + m2) * r0, 0.0])  # těleso 2

# Počáteční oběžná rychlost pro (skoro) kruhovou dráhu
v_circ = np.sqrt(G * (m1 + m2) / r0)

# Rychlosti kolmé na spojnicu, opačné směry, opět se zachováním těžiště
v1 = np.array([0.0, -m2 / (m1 + m2) * v_circ])
v2 = np.array([0.0,  m1 / (m1 + m2) * v_circ])

# Časová nastavení
dt = 60 * 60 * 6      # krok simulace: 6 hodin
T_total = 365 * 24 * 60 * 60   # celkový čas: 1 rok (s)
N_steps = int(T_total / dt)

# ==========================
# Příprava úložiště drah
# ==========================

r1_hist = np.zeros((N_steps, 2))
r2_hist = np.zeros((N_steps, 2))
t_hist = np.zeros(N_steps)

# ==========================
# Funkce pro výpočet zrychlení
# ==========================

def accelerations(r1, r2):
    """
    Spočítá zrychlení obou těles podle Newtonovy gravitace.
    """
    r_vec = r2 - r1
    dist = np.linalg.norm(r_vec)
    # aby se nepropadlo při extrémně malé vzdálenosti
    if dist == 0:
        return np.zeros(2), np.zeros(2)

    # velikost gravitační síly
    a1 =  G * m2 / dist**3 * r_vec   # zrychlení tělesa 1
    a2 = -G * m1 / dist**3 * r_vec   # zrychlení tělesa 2
    return a1, a2

# ==========================
# Integrace pohybu (velocity Verlet)
# ==========================

# počáteční zrychlení
a1, a2 = accelerations(r1, r2)

for i in range(N_steps):
    t = i * dt
    t_hist[i] = t

    r1_hist[i] = r1
    r2_hist[i] = r2

    # Update pozic
    r1_new = r1 + v1 * dt + 0.5 * a1 * dt**2
    r2_new = r2 + v2 * dt + 0.5 * a2 * dt**2

    # Spočti nové zrychlení pro nové pozice
    a1_new, a2_new = accelerations(r1_new, r2_new)

    # Update rychlostí
    v1_new = v1 + 0.5 * (a1 + a1_new) * dt
    v2_new = v2 + 0.5 * (a2 + a2_new) * dt

    # Posuň do dalšího kroku
    r1, r2 = r1_new, r2_new
    v1, v2 = v1_new, v2_new
    a1, a2 = a1_new, a2_new

# ==========================
# Vykreslení drah (statický graf)
# ==========================

fig, ax = plt.subplots(figsize=(8, 8))
ax.plot(r1_hist[:, 0], r1_hist[:, 1], label="Těleso 1 (např. Slunce)")
ax.plot(r2_hist[:, 0], r2_hist[:, 1], label="Těleso 2 (např. planeta)")

ax.set_aspect('equal', 'box')
ax.set_xlabel("x (m)")
ax.set_ylabel("y (m)")
ax.set_title("Dvoutělesový problém – dráhy těles")
ax.grid(True)
ax.legend()

# ==========================
# Animace drah
# ==========================

body1, = ax.plot([], [], 'yo', markersize=10)
body2, = ax.plot([], [], 'bo', markersize=6)
trail2, = ax.plot([], [], 'b-', linewidth=1, alpha=0.6)

def init():
    body1.set_data([], [])
    body2.set_data([], [])
    trail2.set_data([], [])
    return body1, body2, trail2

def update(frame):
    # index snížíme, aby animace nebyla extrémně dlouhá
    idx = frame * 5
    if idx >= N_steps:
        idx = N_steps - 1

    x1, y1 = r1_hist[idx]
    x2, y2 = r2_hist[idx]

    body1.set_data(x1, y1)
    body2.set_data(x2, y2)
    trail2.set_data(r2_hist[:idx, 0], r2_hist[:idx, 1])

    return body1, body2, trail2

frames = N_steps // 5
ani = FuncAnimation(fig, update, frames=frames,
                    init_func=init, interval=30, blit=True)

plt.show()
