import numpy as np
import matplotlib.pyplot as plt

# --- Parameters ---
g = 9.81          # gravity (m/s^2)
dt = 0.01         # time step (s)
t_max = 5.0       # maximum simulation time (s)

# Initial speed and angle
v0 = 20.0         # initial speed (m/s)
angle_deg = 45.0  # launch angle (degrees)
angle_rad = np.deg2rad(angle_deg)

# Initial conditions
x = 0.0
y = 0.0
vx = v0 * np.cos(angle_rad)
vy = v0 * np.sin(angle_rad)

xs = []
ys = []

t = 0.0
while t < t_max:
    xs.append(x)
    ys.append(y)

    # Stop if the projectile hits the ground
    if y < 0:
        break

    # --- Update velocities (Euler) ---
    vy = vy - g * dt  # vertical velocity changes
    # vx stays constant (no air resistance)

    # --- Update positions ---
    x = x + vx * dt
    y = y + vy * dt

    # Advance time
    t += dt

plt.figure()
plt.plot(xs, ys, label="Trajectory")
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.title(f"Projectile motion (v0={v0} m/s, angle={angle_deg}°)")
plt.legend()
plt.grid(True)
plt.show()