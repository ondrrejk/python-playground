import numpy as np
import matplotlib.pyplot as plt

# ==========================
# Parametry
# ==========================

T0 = 90.0          # počáteční teplota objektu (°C)
T_env = 20.0       # teplota prostředí (°C)
k = 0.1            # koeficient chlazení (1/s)

dt = 0.1           # krok simulace
T_end = 60         # celkový čas (s)

# ==========================
# Numerické řešení (Euler)
# ==========================

times = np.arange(0, T_end, dt)
T_num = np.zeros_like(times)

T = T0
for i, t in enumerate(times):
    T_num[i] = T
    dTdt = -k * (T - T_env)
    T = T + dTdt * dt

# ==========================
# Analytické řešení
# ==========================

t_ana = np.linspace(0, T_end, 500)
T_ana = T_env + (T0 - T_env) * np.exp(-k * t_ana)

# ==========================
# Graf
# ==========================

plt.figure(figsize=(10, 6))

plt.plot(times, T_num, 'o', markersize=3, label="Numerické řešení (Euler)")
plt.plot(t_ana, T_ana, '-', label="Analytické řešení")

plt.title("Newtonův zákon chlazení – simulace")
plt.xlabel("čas (s)")
plt.ylabel("teplota (°C)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
