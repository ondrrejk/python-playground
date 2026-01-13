import numpy as np
import matplotlib.pyplot as plt

# ==========================
# Obecná funkce pro vykreslení fraktálu
# ==========================

def compute_fractal(xmin, xmax, ymin, ymax,
                    width=800, height=600,
                    max_iter=200,
                    c_constant=None):
    """
    Pokud c_constant is None -> Mandelbrotova množina.
    Pokud c_constant je komplexní číslo -> Julia množina pro dané c.
    """
    # Vytvoření mřížky komplexních čísel
    re = np.linspace(xmin, xmax, width)
    im = np.linspace(ymin, ymax, height)
    Re, Im = np.meshgrid(re, im)
    Z = Re + 1j * Im

    if c_constant is None:
        # Mandelbrot: z0 = 0, c = Z
        C = Z.copy()
        Z = np.zeros_like(C, dtype=complex)
    else:
        # Julia: z0 = Z, c = konstanta
        C = np.full_like(Z, c_constant, dtype=complex)

    # Iterace
    escape_iter = np.zeros(Z.shape, dtype=int)
    mask = np.ones(Z.shape, dtype=bool)  # které body ještě "žijí"

    for i in range(max_iter):
        Z[mask] = Z[mask] * Z[mask] + C[mask]
        escaped = np.abs(Z) > 2
        newly_escaped = escaped & mask
        escape_iter[newly_escaped] = i
        mask &= ~newly_escaped

    escape_iter[mask] = max_iter
    return escape_iter


def plot_fractal(data, xmin, xmax, ymin, ymax, title="Fraktál"):
    plt.figure(figsize=(8, 6))
    plt.imshow(data, extent=[xmin, xmax, ymin, ymax],
               origin="lower", cmap="turbo")
    plt.colorbar(label="Počet iterací do úniku")
    plt.xlabel("Re")
    plt.ylabel("Im")
    plt.title(title)
    plt.tight_layout()
    plt.show()


# ==========================
# Ukázka: Mandelbrotova množina
# ==========================

def mandelbrot_demo():
    # Základní pohled
    xmin, xmax = -2.5, 1.0
    ymin, ymax = -1.5, 1.5
    max_iter = 300

    data = compute_fractal(xmin, xmax, ymin, ymax,
                           width=1000, height=800,
                           max_iter=max_iter,
                           c_constant=None)
    plot_fractal(data, xmin, xmax, ymin, ymax,
                 title="Mandelbrotova množina")


# ==========================
# Ukázka: Julia množina pro různé c
# ==========================

def julia_demo(c):
    xmin, xmax = -1.5, 1.5
    ymin, ymax = -1.5, 1.5
    max_iter = 300

    data = compute_fractal(xmin, xmax, ymin, ymax,
                           width=1000, height=800,
                           max_iter=max_iter,
                           c_constant=c)
    title = f"Julia množina pro c = {c.real:.3f} + {c.imag:.3f}i"
    plot_fractal(data, xmin, xmax, ymin, ymax, title=title)


# ==========================
# Jednoduché „menu“ v konzoli
# ==========================

def main():
    while True:
        print("\n=== GENERÁTOR FRAKTÁLŮ ===")
        print("1) Mandelbrotova množina (základní pohled)")
        print("2) Julia množina (zadáš c)")
        print("3) Mandelbrot – ruční zoom (zadáš rozsahy)")
        print("4) Konec")

        choice = input("Vyber možnost (1–4): ").strip()

        if choice == "4":
            print("Konec.")
            break

        elif choice == "1":
            mandelbrot_demo()

        elif choice == "2":
            print("Zadej reálnou a imaginární část c (např. -0.7 0.27015):")
            try:
                re_str, im_str = input("c_re c_im: ").split()
                c = complex(float(re_str), float(im_str))
            except Exception:
                print("Špatný vstup, používám c = -0.7 + 0.27015i.")
                c = complex(-0.7, 0.27015)
            julia_demo(c)

        elif choice == "3":
            print("Zadej rozsah pro Re a Im (např. -2 1 -1.5 1.5):")
            try:
                xmin, xmax, ymin, ymax = map(float, input("xmin xmax ymin ymax: ").split())
            except Exception:
                print("Špatný vstup, používám výchozí rozsah.")
                xmin, xmax, ymin, ymax = -2.5, 1.0, -1.5, 1.5

            max_iter_input = input("Maximální počet iterací (default 300): ").strip()
            if max_iter_input == "":
                max_iter = 300
            else:
                try:
                    max_iter = int(max_iter_input)
                except ValueError:
                    max_iter = 300

            data = compute_fractal(xmin, xmax, ymin, ymax,
                                   width=1000, height=800,
                                   max_iter=max_iter,
                                   c_constant=None)
            plot_fractal(data, xmin, xmax, ymin, ymax,
                         title=f"Mandelbrot – zoom\nRe∈[{xmin}, {xmax}], Im∈[{ymin}, {ymax}]")

        else:
            print("Neplatná volba.")


if __name__ == "__main__":
    main()
