import numpy as np
import matplotlib.pyplot as plt

# ==========================
# Parametry signálu
# ==========================

fs = 2000          # vzorkovací frekvence (Hz)
T = 1.0            # délka signálu (s)
N = int(fs * T)    # počet vzorků
t = np.linspace(0, T, N, endpoint=False)

# Vytvoření signálu: kombinace sinusů
f1 = 50    # Hz
f2 = 120   # Hz
f3 = 300   # Hz

signal = (
    1.0 * np.sin(2 * np.pi * f1 * t) +
    0.5 * np.sin(2 * np.pi * f2 * t) +
    0.2 * np.sin(2 * np.pi * f3 * t)
)

# ==========================
# Fourierova transformace
# ==========================

fft_vals = np.fft.fft(signal)
freqs = np.fft.fftfreq(N, 1/fs)

# Pouze kladné frekvence (reálný signál → spektrum je symetrické)
idx = freqs >= 0
freqs_pos = freqs[idx]
fft_pos = np.abs(fft_vals[idx]) * 2 / N   # normalizace amplitudy

# ==========================
# Vykreslení
# ==========================

plt.figure(figsize=(12, 6))

# Časová oblast
plt.subplot(2, 1, 1)
plt.plot(t, signal)
plt.title("Časová oblast – signál")
plt.xlabel("čas (s)")
plt.ylabel("amplituda")
plt.grid(True)

# Frekvenční oblast
plt.subplot(2, 1, 2)
plt.stem(freqs_pos, fft_pos, use_line_collection=True)
plt.title("Frekvenční spektrum (FFT)")
plt.xlabel("frekvence (Hz)")
plt.ylabel("amplituda")
plt.xlim(0, 500)  # omezíme na přehledný rozsah
plt.grid(True)

plt.tight_layout()
plt.show()
