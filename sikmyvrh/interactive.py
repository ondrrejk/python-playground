import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact, FloatSlider

# Interaktivní funkce
def plot_function(A=1.0, B=1.0, C=0.0, xmin=-10, xmax=10):
    x = np.linspace(xmin, xmax, 1000)
    y = A * np.sin(B * x + C)

    plt.figure(figsize=(8, 4))
    plt.plot(x, y, label=f"A·sin(Bx + C)")
    plt.title("Interaktivní vizualizace funkce")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.ylim(-max(1, abs(A))*1.2, max(1, abs(A))*1.2)
    plt.show()

# Posuvníky
interact(
    plot_function,
    A=FloatSlider(min=0, max=5, step=0.1, value=1, description="A"),
    B=FloatSlider(min=0, max=5, step=0.1, value=1, description="B"),
    C=FloatSlider(min=-3.14, max=3.14, step=0.1, value=0, description="C"),
    xmin=FloatSlider(min=-20, max=0, step=1, value=-10, description="xmin"),
    xmax=FloatSlider(min=0, max=20, step=1, value=10, description="xmax"),
)
