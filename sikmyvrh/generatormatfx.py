import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# ===========================
# Nastavení symbolu a prostředí
# ===========================

x = sp.symbols('x')

# Předpřipravené funkce jako sympy výrazy
PREDEFINED = {
    "1": ("sin(x)", sp.sin(x)),
    "2": ("cos(x)", sp.cos(x)),
    "3": ("exp(x)", sp.exp(x)),
    "4": ("log(x)", sp.log(x)),   # přirozený logaritmus
}


def choose_function():
    print("\n=== GENERÁTOR FUNKCÍ ===")
    print("1) sin(x)")
    print("2) cos(x)")
    print("3) exp(x)")
    print("4) log(x)")
    print("5) Vlastní funkce (např. sin(x)*exp(-x), x**2 + 3*x - 1, ...)")
    choice = input("Vyber možnost (1-5): ")

    if choice in PREDEFINED:
        label, expr = PREDEFINED[choice]
        return expr, label
    elif choice == "5":
        user_str = input("Zadej funkci f(x) (v syntaxi Python/SymPy, např. sin(x)*exp(-x)): ")
        try:
            expr = sp.sympify(user_str)
        except Exception as e:
            print("Chyba při parsování výrazu:", e)
            return None, None
        return expr, str(expr)
    else:
        print("Neplatná volba.")
        return None, None


def get_domain(expr):
    """
    Zeptá se uživatele na interval vykreslení.
    Pro log a podobné může být dobré zvolit kladný interval.
    """
    print("\nZadej interval pro x (např. -5 5):")
    s = input("xmin xmax: ")
    try:
        xmin_str, xmax_str = s.split()
        xmin = float(xmin_str)
        xmax = float(xmax_str)
    except Exception:
        print("Neplatný vstup, používám výchozí interval x ∈ [-5, 5].")
        xmin, xmax = -5.0, 5.0
    return xmin, xmax


def compute_numeric(expr, xmin, xmax, n_points=400):
    """
    Převede sympy výraz na numerickou funkci a spočítá hodnoty v daném intervalu.
    """
    f_lambd = sp.lambdify(x, expr, modules=["numpy"])
    xs = np.linspace(xmin, xmax, n_points)

    # ochrana před NaN/inf (log(neg), 1/0, ...)
    try:
        ys = f_lambd(xs)
        ys = np.array(ys, dtype=float)
    except Exception:
        # kdyby se něco rozsypalo, zkusíme bod po bodu
        ys = np.array([float(f_lambd(xi)) if np.isfinite(f_lambd(xi)) else np.nan for xi in xs])

    return xs, ys


def find_roots(expr, xmin, xmax, n_initial=50):
    """
    Hrubé hledání nulových bodů v intervalu [xmin, xmax].
    Použije několik startovacích bodů a sympy nsolve, kde to půjde.
    Výstup: seřazený seznam reálných kořenů v intervalu.
    """
    roots = []
    for guess in np.linspace(xmin, xmax, n_initial):
        try:
            r = sp.nsolve(expr, guess)
            r_val = float(r)
            # zkontrolujeme, že je v intervalu a není duplikát
            if xmin <= r_val <= xmax:
                if all(abs(r_val - rr) > 1e-3 for rr in roots):
                    roots.append(r_val)
        except Exception:
            continue

    roots = sorted(roots)
    return roots


def main():
    expr, label = choose_function()
    if expr is None:
        return

    xmin, xmax = get_domain(expr)

    # Derivace
    deriv_expr = sp.diff(expr, x)

    # Numerické hodnoty funkce a derivace
    xs, ys = compute_numeric(expr, xmin, xmax)
    _, dys = compute_numeric(deriv_expr, xmin, xmax)

    # Nulové body
    print("\nChceš hledat nulové body f(x) = 0 v daném intervalu?")
    do_roots = input("(y/n): ").lower().strip() == 'y'
    roots = []
    if do_roots:
        print("Hledám nulové body... (může chvíli trvat)")
        roots = find_roots(expr, xmin, xmax)
        if roots:
            print("Nalezené nulové body (přibližně):")
            for r in roots:
                print(f"x ≈ {r:.5f}")
        else:
            print("V zadaném intervalu se nepodařilo najít žádné reálné kořeny.")

    # Vykreslení
    plt.figure(figsize=(10, 7))

    # f(x)
    plt.plot(xs, ys, label=f"f(x) = {label}", color="blue")

    # f'(x)
    plt.plot(xs, dys, label=f"f'(x)", color="orange", linestyle="--")

    # nulové body, pokud jsou
    if roots:
        f_lambd = sp.lambdify(x, expr, modules=["numpy"])
        y_roots = [f_lambd(r) for r in roots]
        plt.scatter(roots, y_roots, color="red", zorder=5, label="Nulové body")

    # osa x, y
    plt.axhline(0, color='black', linewidth=0.8)
    plt.axvline(0, color='black', linewidth=0.8)

    plt.title("Funkce a její derivace")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

    print("\nSymbolická derivace:")
    print(f"f(x) = {expr}")
    print(f"f'(x) = {deriv_expr}")


if __name__ == "__main__":
    main()
