import numpy as np
import matplotlib.pyplot as plt

# Parametry RC obvodu
R = 10_000      # odpor v ohmech (10 kΩ)
C = 100e-6      # kapacita v faradech (100 µF)
V = 5.0         # napájecí napětí ve voltech

tau = R * C     # časová konstanta (s)

# Numerická simulace – Eulerova metoda
dt = tau / 100.0         # krok – dost malý vzhledem k tau
T_end = 5 * tau          # simulujeme do 5τ (už skoro plně nabito)
N = int(T_end / dt)

t_num = np.zeros(N)
Vc_num = np.zeros(N)

Vc = 0.0   # počáteční napětí na kondenzátoru

for i in range(N):
    t = i * dt
    t_num[i] = t
    Vc_num[i] = Vc

    dVc_dt = (V - Vc) / (R * C)
    Vc = Vc + dVc_dt * dt

# Analytické řešení
t_ana = np.linspace(0, T_end, 1000)
Vc_ana = V * (1 - np.exp(-t_ana / (R * C)))

# Vykreslení
plt.figure(figsize=(10, 6))

plt.plot(t_num, Vc_num, 'o', markersize=3, label="Numerické řešení (Euler)")
plt.plot(t_ana, Vc_ana, '-', label="Analytické řešení")

plt.axvline(tau, color='gray', linestyle='--', label=r"t = τ")
plt.axhline(V * (1 - np.exp(-1)), color='gray', linestyle=':', 
            label=r"V_C(τ) ≈ 0,632 V")

plt.title("Nabíjení kondenzátoru v RC obvodu")
plt.xlabel("čas t (s)")
plt.ylabel("napětí na kondenzátoru V_C (V)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

print(f"R = {R} Ω, C = {C} F, τ = {tau:.4f} s")
